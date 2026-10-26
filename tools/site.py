#!/usr/bin/env python3
# report.json for wedgie.dev/clear/report: every descriptor's grade and its functions', plus the criticals both
# second agents confirmed. Usage: tools/site.py <out.json>  (wedgie-dev: public/clear/report.json)
import collections, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from findings import confirmed, load  # noqa: E402

RUBRIC_KEYS = ("grade", "truth", "clarity")


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
    Path(out).write_text(json.dumps(data, separators=(",", ":")))
    print(f"{out}: {len(rows)} descriptors, {Path(out).stat().st_size // 1024} KB")


if __name__ == "__main__":
    main(sys.argv[1])
