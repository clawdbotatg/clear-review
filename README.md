# clear-review

A robot second look at the [ERC-7730 clear-signing registry](https://github.com/ethereum/clear-signing-erc7730-registry).

Two models (Claude and Grok) each review every descriptor against the contract's real code. A descriptor passes when
neither finds anything critical. Passes are signed by one key, once per round.
Any wallet can check that signature and show those descriptors as **🤖 checked**: between "audited" and
"not audited". First user: the [wedgie](https://wedgie.dev) Safe Signer.

Status 2026-10-24: review, sign (rounds + adds) and verify built and tested. Trial run on 20 audited + 3 known-bad descriptors.
No real key or round yet.

## Why

- The registry (at `171b6b5`) has 684 descriptors with 2,572 deployments. 167 descriptors are audited (Cyfrin).
  The rest have no review at all.
- A wallet's only choices today: trust the unaudited ones, or show nothing.
- A robot pass isn't an audit, but it catches wrong labels, hidden amounts and wrong recipients, and says why.

## Use

```sh
./review.py sync                 # clone/pull the registry into registry/, npm ci its scripts
./review.py list                 # work/catalog.json: every descriptor with deployments, and its hash
./review.py run --sample 20      # review (busiest first); no args = everything not yet reviewed
./review.py bundle <file>        # review a PR's test report bundle (not merged: never signed)
./review.py report               # REPORT.md
./sign.py keygen                 # once: the review key, in this Mac's Secure Enclave
./sign.py round                  # one Touch ID: rounds/<n>.json
./sign.py add <file|hash>...     # between rounds, just these passed descriptors: adds/<round>-<k>.json
./sign.py verify                 # check the latest round
./test.py                        # offline tests
```

Secrets go in `.env` (gitignored): `CLAUDE_CODE_OAUTH_TOKEN` (a `claude setup-token`) and `XAI_API_KEY`.
Optional: `SOURCIFY_TOKEN` (fewer 429s). Env: `REVIEWERS` (`claude,grok`), `MODEL` (`claude-sonnet-5-5`),
`EFFORT` (`medium`), `GROK` (`grok-4.6`), `PARALLEL` (4).

## How it works

1. **Sync.** Pull the registry at a commit.
2. **Review** each descriptor with its `includes` merged (the same JSON an auditor hashes). The input is built by
   Sourcify's own `collect.js` and the prompt is Sourcify's `prompt.md`, the ones their PR review uses, plus
   `prompt-extra.md`. We feed it a bundle made from the merged descriptor and its `testsv2` file. Inputs:
   - the descriptor
   - the contract's verified source and ABI (Sourcify)
   - the registry's test transactions and the fields they expect

   Questions:
   - Do the labels match what the code does?
   - Is anything that moves money hidden or mislabeled?
   - Are the token, amount and recipient paths right?
3. **Record** `reviews/<descriptor hash>.json`: result, both answers, model, date, prompt hash.
   The hash is ERC-8176's, so a descriptor that changes upstream is unreviewed again on its own.
   - **pass**: both models reviewed every unit, nothing critical, every contract has verified source,
     nothing they said they could not check. Warnings (shown right, could be clearer) don't fail it.
   - **fail**: a model found something critical.
   - **incomplete**: unverified source, a unit too big, a model error, or something a model could not check.
4. **Sign.** Every passed deployment is a leaf in one Merkle tree. The review key signs `(round, registry commit, root)`.
   One signature per round → `rounds/<round>.json`, with every leaf's proof.
5. **Give back.** Failures and warnings become registry issues or PRs, with the reasons.

## Why one signature per round, not one per descriptor

Small devices check signatures slowly (the wedgie: ~2.2 s for one P-256 check in MicroPython; its Trust M chip
does it in hardware, not yet timed). One signed root is checked once. After that, each descriptor is a Merkle proof: hashes only, fast.
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
- This is outside the ERC-7730 wire format on purpose (the spec allows secp256k1 / Ed25519 only, so far).
  If the spec adds P-256, rounds can move into it.

## For a wallet

- Pin the review public key.
- Get `rounds/<latest>.json`, check its signature once, keep the root.
- Adds: take one only if its round is the one you hold; check it once, keep its root. A newer round drops them.
- For each descriptor: check its proof against the root → show "🤖 checked".
  The leaf has the descriptor hash, so the wallet must know the hash of what it shows (ERC-8176; the wedgie's
  build has to carry it inside its signed data).
- Never show 🤖 checked as "audited".

## Steps

1. ~~`review.py`: one descriptor in, a record out.~~ Trial: 20 audited, 3 known-bad (see REPORT.md).
2. Run the whole registry. Read a sample of passes and fails by hand.
3. ~~`sign.py`: build the tree, sign the root with the Secure Enclave key, write the round.~~ Key made 10-24 (`clear-review.pub`).
4. wedgie: Safe Signer checks the round (wedgie-dev `docs/PLAN-ROBOT-REVIEW.md`).
5. File the failures upstream.

## Open questions

- Re-check Cyfrin's audited set too? Yes for now: it's how we calibrate.
- A Sourcify token for the full run (2,572 deployments; anonymous hits 429s).

MIT.
