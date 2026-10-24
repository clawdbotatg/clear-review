# How we sign, and how a wallet checks it

Status 2026-10-24: built and tested (`sign.py`, `test.py`). Key made. No real round signed yet.
Not yet in any wallet. First wallet: the wedgie Safe Signer (wedgie-dev `docs/PLAN-ROBOT-REVIEW.md`).

## TLDR

- One key signs everything. P-256, held in Austin's Mac's Secure Enclave, Touch ID for every signature.
- **Round:** one signature over a Merkle root of every descriptor deployment that passed review.
  It comes out every so often, and the round number only goes up.
- **Add:** one signature over a few new passed descriptors between rounds. No app update and no new round needed.
- The wallet checks each signature **once** and saves what it signed. After that, each transaction costs only
  a few hashes.
- After one wallet update that pins our key, new descriptors ship with just a signature.

## Why

Without this, a wallet has two choices: ship new descriptors inside an app update (the wedgie today:
`safe_roots.py`), or trust the computer to send them (no trust at all). Hardware wallets fix this by signing the data:

| | What gets signed | How keys change | Old data |
|---|---|---|---|
| Ledger | each descriptor, by Ledger's own keys | Ledger-signed certificates (PKI) | the backend serves the latest |
| Trezor | one Merkle root over all definitions, Ed25519 | firmware update | signed timestamp, the device refuses older |
| **us** | one root per round, plus small adds between rounds | wallet update, for now | round number, the wallet refuses lower |

We copy Trezor (one root, refuse old ones) and add Ledger's one-at-a-time adds for speed.

## The key

- **P-256 (secp256r1), ECDSA over SHA-256.** It's the only curve that's fast on our hardware:
  - The wedgie's Trust M chip checks P-256 in hardware: `optiga.verify`, **181 ms** (measured 10-24, real board,
    `tools/timeprobe.py`; a tampered signature correctly fails).
  - Without that chip: pure Python `p256.verify`, **2.4 s** on the same RP2040. Once per signature.
  - The Trust M has no secp256k1 or Ed25519, so those would be slow everywhere. The Secure Enclave only does P-256.
  - Hash-based signatures (WOTS/XMSS) only need hashes to check, but each key signs once, and the Secure Enclave
    can't hold them. Maybe later, for quantum safety.
- Made by `./sign.py keygen` through `se/clear-review-signer` (Swift, CryptoKit, `.userPresence`).
  The private key never leaves the Secure Enclave. `~/.clear-review/clear-review.key` is an Enclave-wrapped
  blob that only works on that one Mac. Losing the Mac means a new key and a wallet update.
- Public key: `clear-review.pub` (65 bytes, `04 || X || Y`):
  `046547ba38ee30aa55b77c7308f93d5e70def2def67bc9ffff458f511e669a25de268adb3b274a9cdc9783cbc89302566529b52140523e419f51ba3fbf5ed9dac9`
- Not an ERC-8176 attestation: those are secp256k1 (EAS), which hardware can't check fast. The wire format draft
  doesn't pick a curve yet (research doc 27, gap 1). If it picks P-256, rounds can move into it.

## Formats

All hashes are SHA-256. Numbers are big-endian.

```
leaf    = SHA-256(0x00 || chainId (8) || address (20) || descriptor hash (32))
node    = SHA-256(0x01 || smaller || bigger)          the odd one out goes up a level as is
round   = "clear-review/v1\0"     || round (4) || registry commit (20) || root (32)
add     = "clear-review/add/v1\0" || round (4) || registry commit (20) || root (32)
sig     = ECDSA P-256 over SHA-256(message), r || s, 64 bytes
```

- The descriptor hash is ERC-8176's (`clearsig` `descriptor_hash`: JCS + keccak over the descriptor with its
  `includes` merged). If a descriptor changes upstream, its hash changes and it drops out on its own.
- One leaf per deployment (chain + address), not per descriptor. A descriptor is only trusted where it was reviewed.
- Nodes sort the pair, so a proof is just a list of hashes, with no left/right bits. This is the same as wedgie-dev
  `wire/release.py`, so the wallet reuses its proof code.
- The two messages start differently, so an add can't be passed off as a round, or a round as an add (tested).

Files:
- `rounds/<n>.json`: `round, registry, root, key, message, signature, passed, leaves[]`.
  Every leaf has `chainId, address, hash, file, proof`.
- `adds/<round>-<k>.json`: the same fields, plus `add: k`.

## Rules for a wallet

1. Pin `clear-review.pub` in the app.
2. **Round:** check the message matches its round, registry and root, then check the signature. Refuse a round number
   lower than the one saved. Save `(round, root)`.
3. **Add:** take it only if its round equals the saved round. Check it the same way. Save its root next to the round's.
4. A newer round drops every saved add. The next round has every add that still passes. One that doesn't is
   revoked this way.
5. **Per transaction:** work out the descriptor hash, compute the leaf, fold the proof, and check the result equals a
   saved root. Hashes only. The descriptor hash must come from data the wallet trusts (on the wedgie, from
   inside the signed bundle).
6. Show it as **🤖 checked**, sitting between "audited" and "not checked". Never call it audited. Warn, don't block.

## Making one

```sh
./review.py run ...                 # reviews/<hash>.json: pass / fail / incomplete
./sign.py round                     # every pass → rounds/<n>.json, one Touch ID
./sign.py add uniswap/calldata-UniswapV2Router02.json   # file, file name or hash; must have passed
./sign.py verify adds/1-1.json      # or no argument: the latest round
./test.py                           # round, add, tamper cases, with a throwaway Enclave key (no Touch ID)
```

- `add` needs a round to exist. It refuses anything that failed, is incomplete, or wasn't reviewed.
- Only merged registry descriptors get signed. PR bundles (`review.py bundle`) are reviewed but never signed.

## Limits

- One key, one Mac. No second signer yet, and no way to change keys without a wallet update. Later: two keys,
  either one can sign (as wedgie releases do), or a Ledger-style certificate.
- An add for round n stays valid until round n+1 ships. To pull a bad add fast, ship a new round.
- A pass means "two models found nothing critical", not an audit. See `REPORT.md` for what it catches and misses.

## Timing probe

`tools/timeprobe.py`: signs a test message with a throwaway key, then times `p256.verify` and `optiga.verify` on the
board over raw REPL. Read only. The board must be unlocked, and no browser can have its port open.
10-24, real board: `p256.verify` 2,421 ms, `optiga.verify` 181 ms (and a tampered signature fails).
