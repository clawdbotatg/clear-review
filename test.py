#!/usr/bin/env -S uv run -q -p 3.13 --script
# /// script
# dependencies = ["cryptography", "clearsig", "eth-hash[pycryptodome]"]
# ///
# Tests with no network and no model: the signed round (a throwaway Secure Enclave key, no Touch ID), and
# review.py's checks and grade.py's rubric. ./test.py
import copy, importlib.util, json, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name):
    s = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


sign, review, grade = load("sign"), load("review"), load("grade")


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


def test_grade():
    sel = review.selector
    assert sel("transfer(address to, uint256 amount)") == "0xa9059cbb"
    assert review.canon("(address a, uint256[] b)[] c, bytes d") == "(address,uint256[])[],bytes"
    assert review.canon("(address a, uint256[] b) c, (uint8 x)[2][] y") == "(address,uint256[]),(uint8)[2][]"

    def fmt(key, findings=(), cases=(), glance=90, depth=90):
        return {"key": key, "effects": [], "shown": "", "findings": list(findings), "cases": list(cases), "glance": glance, "depth": depth}

    def find(sev, axis="truth", gt=False):
        return {"severity": sev, "axis": axis, "kind": "other", "title": f"{sev} {axis}", "evidence": "", "groundTruth": gt}

    def g(formats, cannot=(), hidden=()):
        return grade.grade({"answer": {"formats": formats, "couldNotCheck": list(cannot)}, "hiddenValue": list(hidden)})
    r = g([fmt("a()"), fmt("b()", [find("warning")])])
    assert r["result"] == "pass" and r["formats"]["a()"]["grade"] == "A" and r["formats"]["b()"]["truth"] == 90, r
    r = g([fmt("a()"), fmt("b()", [find("critical", "completeness")])])
    assert r["result"] == "fail" and r["summary"]["grade"] == "F" and r["formats"]["b()"]["truth"] == 25
    assert g([fmt("a()")], cannot=["the router source"])["result"] == "incomplete"
    assert g([fmt("a()")], hidden=["a()"])["result"] == "fail"                   # payable, @.value never shown
    assert grade.grade({"answer": None})["result"] == "error"
    # Receipts cap truth only when a fixable finding backs the gap; an info (the pool decides) costs nothing.
    case = {"index": 0, "signerEffects": 3, "shownRight": 2, "reader": ["right", "right", "partial"]}
    assert g([fmt("a()", [find("info", "completeness", True)], [case])])["formats"]["a()"]["truth"] == 100
    assert g([fmt("a()", [find("warning", "completeness", True)], [case])])["formats"]["a()"]["truth"] == 67
    # Clarity: 60% blind reader, 40% glance and depth.
    assert g([fmt("a()", cases=[case], glance=50, depth=50)])["formats"]["a()"]["clarity"] == round(0.6 * 100 * 2.5 / 3 + 0.4 * 50)


def test_hidden_value():
    w = Path(tempfile.mkdtemp())
    (w / "contracts/1-0x01").mkdir(parents=True)
    abi = [{"type": "function", "name": "buy", "stateMutability": "payable", "inputs": [{"type": "uint256", "name": "a"}]},
           {"type": "function", "name": "sell", "stateMutability": "nonpayable", "inputs": [{"type": "uint256", "name": "a"}]},
           {"type": "function", "name": "swap", "stateMutability": "payable",
            "inputs": [{"type": "tuple", "name": "d", "components": [{"type": "address", "name": "t"}, {"type": "uint256[]", "name": "p"}]}]}]
    (w / "contracts/1-0x01/abi.json").write_text(json.dumps(abi))
    hides = {"intent": "x", "fields": [{"path": "a", "format": "raw"}]}
    shows = {"intent": "x", "fields": [{"path": "@.value", "format": "amount"}]}
    viadef = {"intent": "x", "fields": [{"$ref": "$.display.definitions.eth"}]}

    def run(formats):
        (w / "descriptor.json").write_text(json.dumps({"display": {"formats": formats, "definitions": {"eth": {"path": "@.value"}}}}))
        return review.hidden_value(w)
    assert run({"buy(uint256 a)": hides, "sell(uint256 a)": hides}) == ["buy(uint256 a)"]
    assert run({"buy(uint256 a)": shows, "swap((address t, uint256[] p) d)": viadef}) == []
    assert run({"swap((address t, uint256[] p) d)": hides}) == ["swap((address t, uint256[] p) d)"]
    assert run({"zap(uint256 a)": hides}) == []                # not in the ABI: left to the agent


def test_tx_input():
    def enc(x):
        if isinstance(x, list):
            b = b"".join(enc(i) for i in x)
            return bytes([0xc0 + len(b)]) + b
        return x if len(x) == 1 and x[0] < 0x80 else bytes([0x80 + len(x)]) + x
    to, data = b"\x11" * 20, bytes.fromhex("a9059cbb")    # short: the list stays under RLP's 56-byte short form
    raw = b"\x02" + enc([b"\x0a", b"", b"\x01", b"\x02", b"\x03", to, b"\x05", data, []])
    t = review.tx_input("0x" + raw.hex(), 1)
    assert (t["chainId"], t["to"], t["value"], t["selector"]) == (10, "0x" + "11" * 20, "5", "0xa9059cbb"), t


if __name__ == "__main__":
    for name, f in list(globals().items()):
        if name.startswith("test_"):
            f()
            print("ok", name)
