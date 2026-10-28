#!/usr/bin/env python3
# dump(v): JSON in the registry's testsv2 style (scalar-only objects inline from depth 3, lists inline when they
# fit 120 columns). Check it round-trips a file before rewriting it: dump(json.loads(s)) + "\n" == s.
import json
W = 120
def dump(v, ind=0, pre=0):
    sp = "  " * ind
    if isinstance(v, dict):
        if v and all(not isinstance(x, (dict, list)) for x in v.values()) and ind >= 3:
            return "{ " + ", ".join(f"{json.dumps(k)}: {json.dumps(x, ensure_ascii=False)}" for k, x in v.items()) + " }"
        if not v: return "{}"
        return "{\n" + ",\n".join(f"{sp}  {json.dumps(k)}: {dump(x, ind + 1, len(sp) + 4 + len(json.dumps(k)))}" for k, x in v.items()) + f"\n{sp}}}"
    if isinstance(v, list):
        if not v: return "[]"
        items = [dump(x, ind + 1) for x in v]
        if all("\n" not in i for i in items):
            inline = "[" + ", ".join(items) + "]"
            if pre + len(inline) + 1 <= W: return inline
        return "[\n" + ",\n".join(f"{sp}  {i}" for i in items) + f"\n{sp}]"
    return json.dumps(v, ensure_ascii=False)
