# Fixing registry descriptors

How we turn a confirmed finding into a PR to ethereum/clear-signing-erc7730-registry. Austin, 10-27: "If we do this,
we need to do this right": show what the screen hides, show what it should show, be sure, double check.

## Pick

- `tools/usage.py`, then `tools/site.py`: the "Fix first" list on wedgie.dev/clear/report (tx/week × how bad).
- Fix only what can cost the signer money: hidden ETH, hidden recipient, wrong amount. Before starting, ask
  "can a dapp use this to take funds?" If no, skip it and say why in one line.
- Skipped, low harm (10-27): Ondo GMTokenManager (Ondo signs the price), Morpho VaultBundlesV1 (hidden slippage bound),
  Gondi MultiSourceLoan (loan data hash-checked on-chain; interest just not shown), Morpho Blue withdraw by shares
  (shares can't be turned into assets in a descriptor; labels say "0 if shares"), Ethena cooldown reset (1-day
  cooldown now; would also break the Ledger attestation).

## Per PR

1. Worktree off the registry: `git -C registry worktree add -b <branch> ../work/pr-<x> origin/master`.
   The Morpho gauntlet files always show as modified (case collision). Never stage them.
2. Read the verified source (cached under `work/<hash>/contracts/<chain>-<address>/`). Quote the lines.
3. Fix the descriptor in the file's own style (one-line or multi-line, as the neighbours are).
4. Tests in `testsv2`, unsigned `rawTx` from `cast mktx --raw-unsigned` (real txs: rebuild from `cast tx` fields).
   Add `from` only when the format uses `@.from`. Label made-up cases "synthetic". Rewrite test files with
   `tools/fmt_tests.py` so the diff is only the change.
5. Before/after: run Sourcify's runner (`node runner/dist/cli.js <tests> -o out`) once with the old descriptor, once
   with the new. Picture: `tools/beforeafter.py spec.json page.html`, then `tools/shot.mjs page.html out.png`
   (needs playwright-core: copy it into wedgie-dev/tools and run it from there). Picture goes in `docs/prs/`.
6. Prove the harm on a mainnet fork: anvil `--fork-url` Alchemy (never a public RPC), `anvil_impersonateAccount`
   (Binance `0x28C6…1d60` holds USDC), `anvil_setCode` for stand-in contracts. Check the calldata in the test's
   `rawTx` is the calldata you ran.
7. `erc7730 lint --require-verified` before and after (`uv venv --python 3.12`; 3.15 can't install it). Same warnings,
   no new errors.
8. Double check: Claude (`claude -p --model claude-opus-5-5 --effort high --allowedTools Read Grep Glob`, scrubbed env,
   `CLAUDE_CODE_OAUTH_TOKEN` from `.env`) and Codex (`codex exec -s read-only`), same ask file: source, old and new
   descriptor, screens, claim, fork result; reply as JSON with a verdict. Repeat until both say ship.
9. PR as **clawdbotatg** only: `gh auth switch --user clawdbotatg`, push to its fork with
   `-c credential.helper='!gh auth git-credential'`, `gh pr create -R ethereum/clear-signing-erc7730-registry
   --head clawdbotatg:<branch>`, then switch back to austintgriffith. One entity per PR. If the descriptor has a
   `sigs/` file, the change breaks that attestation: delete it and say so.

## Learned

- The standard fix for hidden ETH: `{"path": "@.value", "label": "Native Value Sent", "format": "amount",
  "visible": "always"}` after the input amount (1inch, LiFi already use it). Reviewers suggest `ifNotIn ["0"]`;
  we keep `always` so every PR matches.
- Never label a calldata address with what it should be ("Clipper Exchange"). Say what happens: "Funds Sent To".
- `addressName` needs `params` or lint fails. `types: ["contract"]` lets a wallet warn on an EOA.
- Bundles (`#.bundle.[]`): a group with `iteration: "bundled"` shows target, ETH and action together. Inside the
  group, `calleePath`/`amountPath` must be relative (`"to"`, `"value"`); absolute `#.bundle.[].to` stops nested
  decoding in the runner. Do the same for `reenter`-style entry points: they run inside a user's bundle.
- A test case must be a tx that can run. Reviewers caught a nested multicall that always reverts.
- Codex reads the scratch test files too; say which file is the registry's.
- gitleaks flags tx hashes as private keys. Drop the optional `txHash` field rather than bypass the hook.
- Change the sentence too when there is an `interpolatedIntent`: a wallet may show only that.
- Claims a reviewer makes are not proof: unoswap's "hidden first pool" didn't hold (the next real pair reverts).
  Reason it through, then ask them again.

## Open PRs (10-27)

| PR | What |
|---|---|
| [#3158](https://github.com/ethereum/clear-signing-erc7730-registry/pull/3158) | 1inch V6: ETH on swap, permitAndCall |
| [#3159](https://github.com/ethereum/clear-signing-erc7730-registry/pull/3159) | Uniswap SwapRouter02: ETH on swaps |
| [#3160](https://github.com/ethereum/clear-signing-erc7730-registry/pull/3160) | KyberSwap MetaAggregationRouterV2: ETH on swap |
| [#3162](https://github.com/ethereum/clear-signing-erc7730-registry/pull/3162) | Paraswap AugustusV6.2: fees on swapExactAmountInPro |
| [#3163](https://github.com/ethereum/clear-signing-erc7730-registry/pull/3163) | 1inch V5: ETH on swaps, clipper target |
| [#3164](https://github.com/ethereum/clear-signing-erc7730-registry/pull/3164) | Morpho Bundler3: ETH, targets, forwarded ETH |

#3157 and #3161 (Uniswap V3 positions, SwapRouter02 multicall) are new descriptors, not fixes.
