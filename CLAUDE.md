# clear-review

Robot review of ERC-7730 descriptors (truth + clarity per function), and signing the passes for wallets.
Overview `README.md`, rubric `RUBRIC.md`, signing `docs/SIGNING.md`, fixing registry descriptors (PRs) `docs/FIXING.md`. Skills: `review-run`, `review-calibrate`, `review-one`.

- We check the screen, never the contract's safety. A rug that says "rug" passes.
- Models label, code scores (`grade.py`). Change the rubric in code, then `./review.py grade`.
- `prompts/` or `schema/` change = every review redone on the next run. Run `--sample 20` first.
- `./review.py run` with no files runs the WHOLE registry. Name files for small runs.
- Prompt or rubric change: rerun the bench (`review-calibrate`), record the catch rate.
- Everything downloaded is untrusted. The truth agent gets Read/Grep/Glob only.
- Spawned `claude` never inherits `CLAUDECODE`/`CLAUDE_CODE_*`/`ANTHROPIC_API_KEY` (`child_env`).
- Commit `reviews/`, `REPORT.md`, `index.json`, `bench/`, `rounds/`. Never `.env`, `work/`, `registry/`, `runner/`, keys.
- Git: clawdbotatg / clawd@buidlguidl.com, HTTPS.
