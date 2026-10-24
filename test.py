#!/usr/bin/env -S uv run -q -p 3.13 --script
# /// script
# dependencies = ["cryptography", "clearsig"]
# ///
# Tests with no network and no model: the signed round (a throwaway Secure Enclave key, no Touch ID), and
# review.py's parsing. ./test.py
import copy, importlib.util, json, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    s = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


sign, review = load("sign"), load("review")


def test_round():
    tmp = Path(tempfile.mkdtemp())
    (tmp / "reviews").mkdir()
    cat = {"registry": "ab" * 20, "descriptors": []}
    for i, result in enumerate(["pass", "pass", "fail", "incomplete", "pass"]):
        h = "0x%064x" % (i + 1)
        cat["descriptors"].append({"file": f"f{i}.json", "hash": h, "deployments":
                                   [{"chainId": 1 + j, "address": "0x%040x" % (i * 10 + j)} for j in range(i + 1)]})
        (tmp / "reviews" / f"{h}.json").write_text(json.dumps({"result": result}))
    r = sign.build(cat, tmp / "reviews", 3)
    assert r["passed"] == 1 + 2 + 5, r["passed"]
    key = tmp / "t.key"
    pub = subprocess.run([str(ROOT / "se/clear-review-signer"), "create", str(key), "--no-touch"], check=True, capture_output=True, text=True).stdout.strip()
    r["signature"] = subprocess.run([str(ROOT / "se/clear-review-signer"), "sign", str(key), r["message"]], check=True, capture_output=True, text=True).stdout.strip()
    assert sign.verify(r, pub) is None
    bad = copy.deepcopy(r); bad["round"] = 2
    assert sign.verify(bad, pub) == "message does not match round, registry and root"
    bad = copy.deepcopy(r); bad["leaves"][0]["hash"] = "0x" + "ff" * 32
    assert sign.verify(bad, pub).startswith("bad proof")
    bad = copy.deepcopy(r); bad["leaves"][0]["chainId"] = 999
    assert sign.verify(bad, pub).startswith("bad proof")
    other = subprocess.run([str(ROOT / "se/clear-review-signer"), "create", str(tmp / "o.key"), "--no-touch"], check=True, capture_output=True, text=True).stdout.strip()
    assert sign.verify(r, other) == "bad signature"
    add = sign.build(sign.pick(cat, tmp / "reviews", ["f4.json"]), tmp / "reviews", 3, sign.ADD)
    add["add"] = 1
    assert add["passed"] == 5
    add["signature"] = subprocess.run([str(ROOT / "se/clear-review-signer"), "sign", str(key), add["message"]], check=True, capture_output=True, text=True).stdout.strip()
    assert sign.verify(add, pub) is None
    bad = copy.deepcopy(add); del bad["add"]                     # an add never passes as a round
    assert sign.verify(bad, pub) == "message does not match round, registry and root"
    bad = copy.deepcopy(r); bad["add"] = 1                       # nor a round as an add
    assert sign.verify(bad, pub) == "message does not match round, registry and root"
    for w in ("f2.json", "f3.json", "nope.json"):                # failed, incomplete, unknown: never added
        try:
            sign.pick(cat, tmp / "reviews", [w]); assert False, w
        except SystemExit:
            pass
    one = sign.build({**cat, "descriptors": cat["descriptors"][:1]}, tmp / "reviews", 1)
    assert one["leaves"][0]["proof"] == [] and one["root"] == sign.leaf(1, "0x" + "00" * 20, "0x%064x" % 1).hex()


def test_review_parsing():
    ans = "# Review\n\n## Critical\n\nNone.\n\n## Warning\n\n### a is wrong\n\n- x\n\n### b is wrong\n\n## Info\n\nNone.\n"
    assert review.well_formed(ans) and not review.limited(ans)
    assert review.counts(ans) == {"critical": [], "warning": ["a is wrong", "b is wrong"], "info": []}
    assert review.limited(ans + "\n## What could not be reviewed\n\nthe proxy\n")
    u = lambda **by: {"unverified": [], "by": {k: {"critical": v, "limited": False} for k, v in by.items()}}
    assert review.verdict([u(claude=[], grok=[])], []) == "pass"
    assert review.verdict([u(claude=[], grok=["x"])], []) == "fail"
    assert review.verdict([u(claude=[], grok=[])], [{"why": "model error"}]) == "incomplete"
    assert review.verdict([{**u(claude=[]), "unverified": ["1:0x"]}], []) == "incomplete"
    assert review.verdict([], []) == "error"
    assert review.selector("transfer(address to, uint256 amount)") == "0xa9059cbb"
    assert review.canon("(address a, uint256[] b)[] c, bytes d") == "(address,uint256[])[],bytes"


def test_tx_input():
    def enc(x):
        if isinstance(x, list):
            b = b"".join(enc(i) for i in x)
            return bytes([0xc0 + len(b)]) + b
        return x if len(x) == 1 and x[0] < 0x80 else bytes([0x80 + len(x)]) + x
    to, data = b"\x11" * 20, bytes.fromhex("a9059cbb")    # short: the list stays under RLP's 56-byte short form
    raw = b"\x02" + enc([b"\x0a", b"", b"\x01", b"\x02", b"\x03", to, b"\x05", data, []])
    t = review.tx_input("0x" + raw.hex(), 1)
    assert (t["chainId"], t["to"], t["value"], t["selector"], t["txType"]) == (10, "0x" + "11" * 20, "5", "0xa9059cbb", "eip1559"), t


if __name__ == "__main__":
    for name, f in list(globals().items()):
        if name.startswith("test_"):
            f()
            print("ok", name)
