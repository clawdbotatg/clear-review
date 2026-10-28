# before/after picture page: beforeafter.py <spec.json> <out.html>
# spec: {"title", "note", "owner", "cases": [{"h", "before": {"intent", "fields": [[label, value]]}, "after": {...}, "new": [labels], "beforeH", "afterH"}]}
import html, json, sys
s = json.load(open(sys.argv[1]))
CSS = """body{margin:0;font:16px -apple-system,system-ui,sans-serif;background:#f4f4f1;color:#1a1b1a;width:860px;padding:24px}
h2{margin:0 0 4px;font-size:22px} p{margin:0 0 16px;color:#555} h4{margin:18px 0 8px;font-size:16px}
.row{display:flex;gap:20px} .card{flex:1} h3{margin:0 0 8px;font-size:15px}
.scr{background:#fff;border:1px solid #ddd;border-radius:14px;padding:14px}
.i{font-weight:800;font-size:20px} .o{color:#777;font-size:13px;margin-bottom:8px}
.f{display:flex;justify-content:space-between;gap:12px;padding:7px 0;border-top:1px solid #eee;font-size:14px}
.f span{color:#666;white-space:nowrap} .f b{text-align:right;word-break:break-all}
.sub{margin-left:14px;border-left:3px solid #ddd;padding-left:8px}
.new{background:#ffe9e8;margin:0 -8px;padding:7px 8px;border-radius:6px} .new b{color:#c41d18}"""
e = html.escape
def fields(fs, new):
    out = ""
    for l, v in fs:
        if isinstance(v, dict):
            out += f'<div class="f"><span>{e(l)}</span><b>{e(v["intent"])}</b></div><div class="sub">{fields(v["fields"], new)}</div>'
        else:
            out += f'<div class="f{" new" if l in new else ""}"><span>{e(l)}</span><b>{e(v)}</b></div>'
    return out
def scr(x, new):
    return f'<div class="scr"><div class="i">{e(x["intent"])}</div><div class="o">{e(s["owner"])}</div>{fields(x["fields"], new)}</div>'
body = f'<h2>{e(s["title"])}</h2><p>{e(s["note"])}</p>'
for c in s["cases"]:
    body += (f'<h4>{e(c["h"])}</h4><div class="row"><div class="card"><h3>{e(c.get("beforeH", "Before"))}</h3>{scr(c["before"], [])}</div>'
             f'<div class="card"><h3>{e(c.get("afterH", "After"))}</h3>{scr(c["after"], c["new"])}</div></div>')
open(sys.argv[2], "w").write(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{body}")
