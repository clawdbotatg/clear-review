# clear-review

A robot second look at the [ERC-7730 clear-signing registry](https://github.com/ethereum/clear-signing-erc7730-registry).

A model reviews each descriptor against the contract's real code. Passes are signed by one key, once per round.
Any wallet can check that signature and show those descriptors as **🤖 checked**: between "audited" and
"not audited". First user: the [wedgie](https://wedgie.dev) Safe Signer.

Status 2026-10-24: plan only.

## Why

- The registry has ~6,700 descriptor deployments. ~760 are audited (Cyfrin). The rest have no review at all.
- A wallet's only choices today: trust the unaudited ones, or show nothing.
- A robot pass isn't an audit, but it catches wrong labels, hidden amounts and wrong recipients, and says why.

## How it works

1. **Sync.** Pull the registry at a commit.
2. **Review** each descriptor (its `includes` merged, the same JSON an auditor hashes). Inputs:
   - the descriptor
   - the contract's verified source and ABI (Sourcify)
   - the registry's test transactions and the fields they expect

   Questions:
   - Do the labels match what the code does?
   - Is anything that moves money hidden or mislabeled?
   - Are the token, amount and recipient paths right?
3. **Record** `reviews/<chain>/<address>/<descriptor hash>.json`: pass or fail, model, date, reasons.
   Keyed by hash, so a descriptor that changes upstream is unreviewed again on its own.
4. **Sign.** Every pass is a leaf in one Merkle tree. The review key signs `(root, registry commit, round)`.
   One signature per round → `rounds/<round>.json`.
5. **Give back.** Failures become registry issues or PRs, with the reasons.

## Why one signature per round, not one per descriptor

Small devices check signatures slowly (the wedgie: ~2.2 s for one P-256 check in MicroPython). One signed root
is checked once. After that, each descriptor is a Merkle proof: hashes only, fast.
The round number only goes up, so a wallet can refuse an old round.

## The key

- P-256: fast on hardware wallets and secure elements.
- Only for this. Held in a Mac's Secure Enclave: one Touch ID per round. Public half published here.
- This is outside the ERC-7730 wire format on purpose (the spec allows secp256k1 / Ed25519 only, so far).
  If the spec adds P-256, rounds can move into it.

## For a wallet

- Pin the review public key.
- Get `rounds/<latest>.json`, check its signature once, keep the root.
- For each descriptor: check its proof against the root → show "🤖 checked".
- Never show 🤖 checked as "audited".

## Steps

1. `review.py`: one descriptor in, a record out. Try it on 20 known-good and a few known-bad descriptors.
2. Run the whole registry. Read a sample of passes and fails by hand.
3. `sign.py`: build the tree, sign the root with the Secure Enclave key, write the round.
4. wedgie: Safe Signer checks the round (wedgie-dev `docs/PLAN-ROBOT-REVIEW.md`).
5. File the failures upstream.

## Open questions

- Review all ~6,000 deployments, or the busiest contracts first?
- Re-check Cyfrin's audited set too (a second opinion)?
- Which model? One pass, or two that must agree?

MIT.
