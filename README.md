# clear-review

A robot second look at the [ERC-7730 clear-signing registry](https://github.com/ethereum/clear-signing-erc7730-registry).

A descriptor turns a transaction into the screen you read before signing. This checks that screen, function by
function: **truth** (does it say what really happens to your wallet?) and **clarity** (does a normal person get
it?). Not an audit of the contract: a rug that says "rug" passes. Passes are signed by one key, once per round,
so any wallet can show them as **🤖 checked**. First user: the [wedgie](https://wedgie.dev) Safe Signer.

## How

1. **Real transactions.** 1,120 of the registry's 2,830 test cases are mined txs. `effects.py` reads each one's
   receipt and call trace: every token and ETH movement and approval. That is what happened; the test's screen is
   what the wallet showed.
2. **Blind reader.** Sonnet sees only the screen and says what it thinks will happen.
3. **Truth agent.** `claude -p`, Opus 5.5, high effort, read-only tools. Reads the verified source (Sourcify's
   collector), the mined effects and the reader's answers. Writes findings with evidence, per function, on the
   registry AI review's severity scale.
4. **ABI check.** A payable function whose screen never shows the ETH sent (`@.value`) is an F. No model.
5. **Grades in code** (`grade.py`, [RUBRIC.md](RUBRIC.md)): truth and clarity 0–100 and a letter per function.
   Result: **pass** (no F, nothing blocked the check), **fail** (any F), **incomplete** (code it couldn't see).
6. **Checking the checker** (`mutate.py`). Plant a known lie in a good descriptor, re-render the screen with
   Sourcify's runner, check it's caught. First bench: 5 of 6 (`bench/REPORT.md`).
7. **Second check** (`./review.py verify`, with `--engine codex` too). Every critical of a failed descriptor goes
   to Claude and to Codex, each told to prove it wrong. Both refute it: dropped. Both confirm it:
   `FINDINGS.md` (`tools/findings.py`), for the registry.
   The public page, [wedgie.dev/clear/report](https://wedgie.dev/clear/report):
   `tools/site.py ../wedgie-dev/public/clear/report.json`, then push wedgie-dev.
8. **Sign** the passes (below).

Keyed by the ERC-8176 descriptor hash: a descriptor that changes upstream is unreviewed again on its own.

## Use

```sh
./review.py sync                 # registry + Sourcify's runner
./review.py list                 # work/catalog.json
./review.py run --sample 20      # busiest first; no args = every descriptor not yet reviewed
./review.py run --workers 10     # 10 agents at once, over every plan in TOKENS_ENV
./review.py grade                # recompute every review from saved answers, no model calls
./review.py report               # REPORT.md
./review.py index                # index.json: chain:address:selector → grade
./mutate.py <registry file>      # plant bugs → ./review.py run --bench → ./mutate.py report
./sign.py keygen                 # once: the review key, in this Mac's Secure Enclave
./sign.py round                  # one Touch ID: rounds/<n>.json
./sign.py add <file|hash>...     # between rounds, just these passed descriptors
./sign.py verify                 # check the latest round
./test.py                        # offline tests
```

`.env` (gitignored): `ALCHEMY_API_KEY`; `TOKENS_ENV` = a file of `CLAUDE_TOKEN_<NAME>=` setup-tokens (one per
subscription, `claude setup-token`), or `CLAUDE_CODE_OAUTH_TOKEN`. Optional: `SOURCIFY_TOKEN`, `MODEL`,
`EFFORT`, `READER`, `WORKERS`. Skills for a Claude session: `review-run`, `review-calibrate`, `review-one`.

Output: `reviews/<hash>.json` (result, per-function grades, findings, the full answer), `index.json` (what a
wallet looks up for the one function it shows).

## Why one signature per round, not one per descriptor

Small devices check signatures slowly (the wedgie: 2.4 s for one P-256 check in MicroPython, 0.18 s on its
Trust M chip). One signed root is checked once. After that, each descriptor is a Merkle proof: hashes only, fast.
The round number only goes up, so a wallet can refuse an old round.

## Formats

Full detail (key, round, add, wallet rules, why P-256, how Ledger and Trezor compare): [`docs/SIGNING.md`](docs/SIGNING.md).


- Leaf: `SHA-256(0x00 || chainId (8 bytes BE) || address (20) || descriptor hash (32))`
- Node: `SHA-256(0x01 || smaller || bigger)`, odd one out goes up as is (same as wedgie-dev `release.py`).
- Message: `"clear-review/v1\0" || round (4 bytes BE) || registry commit (20) || root (32)`.
- Add: `"clear-review/add/v1\0" || round || registry commit || root of the added leaves`, same leaves and nodes.
- Signature: ECDSA P-256 over SHA-256(message), `r || s`, 64 bytes.

## The key

- P-256: fast on hardware wallets and secure elements.
- Only for this. Made in and held by a Mac's Secure Enclave (`se/clear-review-signer.swift`): one Touch ID per round. The key file
  (`~/.clear-review/clear-review.key`) is wrapped by the Enclave and useless on any other machine. Public half: `clear-review.pub`.
- Not an ERC-8176 attestation (those are secp256k1). The wire format draft doesn't pick a curve yet;
  if it picks P-256, rounds can move into it.

## For a wallet

- Pin the review public key.
- Get `rounds/<latest>.json`, check its signature once, keep the root.
- Adds: take one only if its round is the one you hold; check it once, keep its root. A newer round drops them.
- For each descriptor: check its proof against the root → show "🤖 checked".
  The leaf has the descriptor hash, so the wallet must know the hash of what it shows (ERC-8176; the wedgie's
  build has to carry it inside its signed data).
- Never show 🤖 checked as "audited".

## Steps

1. ~~`review.py`: one descriptor in, a record out.~~ 10-24: two models, no tools. 10-26: replaced by the truth
   agent + real transactions + blind reader (was clear-score, merged here).
2. Run the whole registry. Read a sample of passes and fails by hand.
3. ~~`sign.py`: build the tree, sign the root with the Secure Enclave key, write the round.~~ Key made 10-24 (`clear-review.pub`).
4. wedgie: Safe Signer checks the round (wedgie-dev `docs/PLAN-ROBOT-REVIEW.md`).
5. File the failures upstream.

## Open questions

- Re-check Cyfrin's audited set too? Yes for now: it's how we calibrate.
- A Sourcify token for the full run (2,572 deployments; anonymous hits 429s).

MIT.
