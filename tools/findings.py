#!/usr/bin/env python3
# FINDINGS.md: every critical both second agents (Claude + Codex) confirmed, grouped by descriptor, for the
# registry. ETH-value-only findings (payable, no @.value field) are listed apart: many are gas-saving `payable`.
import collections, glob, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALUE = ("payable", "@.value", "eth sent", "native value")


def load():
    return sorted((json.loads(Path(f).read_text()) for f in glob.glob(str(ROOT / "reviews/*.json"))), key=lambda r: r["file"])


def confirmed(recs):
    """Criticals both second agents confirmed: {file: (rec, [(claude, codex, original finding)])}, and the
    value-only ones {file: [function names]}."""
    sub, val = collections.OrderedDict(), collections.defaultdict(list)
    for r in recs:
        a = (r.get("verified") or {}).get("findings") or []
        b = (r.get("verifiedCodex") or {}).get("findings") or []
        orig = {(f["key"], x["title"]): x for f in (r.get("answer") or {}).get("formats", []) for x in f["findings"]}
        for x, y in zip(a, b):
            if not x["verdict"] == y["verdict"] == "confirmed":
                continue
            if any(k in x["title"].lower() for k in VALUE):
                val[r["file"]].append(x["format"].split("(")[0])
            else:
                sub.setdefault(r["file"], (r, []))[1].append((x, y, orig.get((x["format"], x["title"]), {})))
    return sub, val


def main():
    recs = load()
    commit = recs[0]["registry"][:7] if recs else "?"
    sub, val = confirmed(recs)
    n = sum(len(v[1]) for v in sub.values())
    L = ["# Confirmed findings", "",
         f"Registry `{commit}`. An Opus agent reviewed every descriptor against the verified source and the registry's",
         "own mined test transactions (receipts), on the AI review's severity scale. Each critical then went to two",
         "more agents, Claude and Codex, told to prove it wrong. Listed here: criticals **both** confirmed.",
         f"{n} in {len(sub)} descriptors. Full answers: `reviews/<descriptor hash>.json`. Method: `README.md`.", ""]
    for file, (r, xs) in sub.items():
        L += [f"## `{file}`" + ("  (audited)" if r["auditedBy"] else ""), ""]
        for x, y, o in xs:
            L += [f"- **{x['format'].split('(')[0]}**: {x['title']}",
                  f"  - Code: {(x.get('quote') or o.get('evidence') or '').strip()[:500]}",
                  f"  - Second check: {x['reason']} / {y['reason']}"]
            if o.get("fix"):
                L.append(f"  - Fix: {o['fix'].strip()[:400]}")
        L.append("")
    L += ["## Payable functions with no ETH field", "",
          "Both agents confirmed these functions keep or forward ETH sent with the call, and no field shows it.",
          "Many are `payable` only to save gas (Solady). Fix: add an `@.value` field, or note it is always 0.", ""]
    L += [f"- `{f}`: {', '.join(sorted(set(fs)))}" for f, fs in sorted(val.items())]
    (ROOT / "FINDINGS.md").write_text("\n".join(L) + "\n")
    print(f"{n} findings in {len(sub)} descriptors; {sum(len(v) for v in val.values())} value-only in {len(val)}")


if __name__ == "__main__":
    main()
