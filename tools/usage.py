#!/usr/bin/env python3
# Mainnet use per function, from Kaan's dashboard (erc7730.sourcify.dev): the busiest contracts of the last 7 days,
# their top selectors and tx counts. Writes work/usage.json {"tx": {"1:<address>:<selector>": txCount,
# "1:<address>": txCount}, "sig": {"<selector>": "name(types)"}}.
# Calldata only: EIP-712 descriptors (permits, Safe, orders) never show up as txs.
import json, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://erc7730.sourcify.dev/api/live/ranking?window=7d&limit=1000&offset={}"
PAGES = int(sys.argv[1]) if len(sys.argv) > 1 else 10   # top 10,000 contracts: ~93% of mainnet txs


def main():
    out, sig, meta = {}, {}, None
    for p in range(PAGES):
        d = json.load(urllib.request.urlopen(API.format(p * 1000), timeout=120))
        meta = meta or d["window"]
        for c in d["contracts"]:
            a = c["toAddress"].lower()
            out[f"1:{a}"] = c["txCount"]
            for s in c["topSelectors"]:
                out[f"1:{a}:{s['selector']}"] = s["txCount"]
                sig[s["selector"]] = s.get("functionSig") or ""
        print(f"page {p + 1}: down to {d['contracts'][-1]['txCount']} tx/week", file=sys.stderr)
    (ROOT / "work").mkdir(exist_ok=True)
    (ROOT / "work/usage.json").write_text(json.dumps({"window": meta, "tx": out, "sig": sig}))
    print(f"work/usage.json: {sum(1 for k in out if k.count(':') == 1)} contracts")


if __name__ == "__main__":
    main()
