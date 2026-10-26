#!/usr/bin/env python3
# report.json for wedgie.dev/clear/report: every descriptor's grade and its functions', plus the criticals both
# second agents confirmed, and "busy": graded functions by mainnet use (work/usage.json, tools/usage.py), worst first.
# Usage: tools/site.py <out.json>  (wedgie-dev: public/clear/report.json)
import collections, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from findings import ROOT, confirmed, load  # noqa: E402

RUBRIC_KEYS = ("grade", "truth", "clarity")
BAD = {"F": 1, "D": 0.5, "C": 0.2}   # how much a tx through a function of this grade counts toward "fix this first"


def busy(rows):
    """[file, function, grade, truth, clarity, worst, tx/week, address] for every graded mainnet function Kaan's
    dashboard saw, worst first: tx × BAD[grade]."""
    u = ROOT / "work/usage.json"
    if not u.exists():
        return None, []
    u = json.loads(u.read_text())
    by_file = {r["file"]: r for r in rows}
    out = []
    for k, v in json.loads((ROOT / "index.json").read_text())["functions"].items():
        tx = u["tx"].get(k)
        if not tx or v["grade"] not in BAD:
            continue
        r, name = by_file[v["file"].removeprefix("registry/")], (u["sig"].get(k.split(":")[2]) or "?").split("(")[0]
        fn = next((f for f in r["fns"] if f[0] == name and f[1] == v["grade"]), None)
        out.append([r["file"], name, v["grade"], v["truth"], v["clarity"], fn[4] if fn else "", tx, k.split(":")[1]])
    out.sort(key=lambda x: -x[6] * BAD[x[2]])
    return u["window"], out


def main(out):
    recs = load()
    sub, val = confirmed(recs)
    rows = []
    for r in recs:
        s = r.get("summary") or {}
        fns = [[k.split("(")[0], v["grade"], v["truth"], v["clarity"], v.get("worst") or ""]
               for k, v in (r.get("formats") or {}).items()]
        found = [{"fn": x["format"].split("(")[0], "title": x["title"],
                  "code": (x.get("quote") or o.get("evidence") or "").strip()[:600],
                  "why": [x["reason"], y["reason"]], "fix": (o.get("fix") or "").strip()[:500]}
                 for x, y, o in sub.get(r["file"], (None, []))[1]]
        rows.append({"file": r["file"].removeprefix("registry/"), "kind": r["kind"],
                     "result": r.get("result", "error"), "audited": bool(r.get("auditedBy")),
                     **{k: s.get(k) for k in RUBRIC_KEYS}, "worst": s.get("worst") or "",
                     "cant": ((r.get("answer") or {}).get("couldNotCheck") or [""])[0][:300],
                     "fns": fns, "found": found, "value": sorted(set(val.get(r["file"], [])))})
    data = {"registry": recs[0]["registry"], "date": max(r["date"] for r in recs)[:10],
            "rubric": recs[0].get("rubric"), "results": collections.Counter(r["result"] for r in rows),
            "grades": collections.Counter(r["grade"] for r in rows),
            "functions": sum(len(r["fns"]) for r in rows), "rows": rows}
    data["usageWindow"], data["busy"] = busy(rows)
    Path(out).write_text(json.dumps(data, separators=(",", ":")))
    print(f"{out}: {len(rows)} descriptors, {Path(out).stat().st_size // 1024} KB")


if __name__ == "__main__":
    main(sys.argv[1])
