#!/usr/bin/env -S uv run -q -p 3.13 --script
# /// script
# dependencies = ["cryptography"]
# ///
# One signed Merkle root per round over every descriptor deployment the robot review passed.
#
#   ./sign.py keygen                     make the review key in this Mac's Secure Enclave (Touch ID), write clear-review.pub
#   ./sign.py round                      build the tree from work/catalog.json + reviews/, sign it (one Touch ID),
#                                        write rounds/<n>.json
#   ./sign.py add <file|hash>...         between rounds: sign just these passed descriptors (one Touch ID),
#                                        write adds/<round>-<k>.json. The next round includes them.
#   ./sign.py verify [<json>]            check the signature against clear-review.pub and every proof (default: latest round)
#
# Leaf    = SHA-256(0x00 || chainId, 8 bytes big-endian || address, 20 bytes || descriptor hash, 32 bytes)
# Node    = SHA-256(0x01 || the smaller hash || the bigger); an odd one out goes up as is (as wedgie-dev release.py)
# Message = "clear-review/v1\0" || round, 4 bytes big-endian || registry commit, 20 bytes || root, 32 bytes
# Add     = "clear-review/add/v1\0" || round || registry commit || root of the added leaves, same sizes.
#           A wallet takes an add only for the round it holds, and drops its adds when a newer round comes.
# Signature: ECDSA P-256 over SHA-256(message), r || s. Env: KEY (default ~/.clear-review/clear-review.key).
import hashlib, json, os, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KEY = Path(os.environ.get("KEY", Path.home() / ".clear-review/clear-review.key"))
PUB = ROOT / "clear-review.pub"
ROUNDS = ROOT / "rounds"
ADDS = ROOT / "adds"
MAGIC = b"clear-review/v1\x00"
ADD = b"clear-review/add/v1\x00"


def leaf(chain, address, dhash):
    return hashlib.sha256(b"\x00" + chain.to_bytes(8, "big") + bytes.fromhex(address[2:]) + bytes.fromhex(dhash[2:])).digest()


def node(a, b):
    return hashlib.sha256(b"\x01" + (a + b if a < b else b + a)).digest()


def tree(leaves):
    """(root, proof(i)) for a list of leaf hashes."""
    levels = [list(leaves)]
    while len(levels[-1]) > 1:
        cur = levels[-1]
        levels.append([node(cur[i], cur[i + 1]) if i + 1 < len(cur) else cur[i] for i in range(0, len(cur), 2)])

    def proof(i):
        out = []
        for lv in levels[:-1]:
            if i ^ 1 < len(lv):
                out.append(lv[i ^ 1])
            i //= 2
        return out
    return levels[-1][0], proof


def fold(h, proof):
    for p in proof:
        h = node(h, p)
    return h


def message(rnd, commit, root, magic=MAGIC):
    return magic + rnd.to_bytes(4, "big") + bytes.fromhex(commit) + root


def passed(catalog, reviews):
    """[(chain, address, hash, file)] for every deployment of every descriptor that passed, sorted by leaf."""
    out = []
    for d in catalog["descriptors"]:
        f = reviews / f"{d['hash']}.json"
        if f.exists() and json.loads(f.read_text())["result"] == "pass":
            out += [(x["chainId"], x["address"], d["hash"], d["file"]) for x in d["deployments"]]
    return sorted(set(out), key=lambda x: leaf(*x[:3]))


def build(catalog, reviews, rnd, magic=MAGIC):
    items = passed(catalog, reviews)
    if not items:
        sys.exit("nothing passed: nothing to sign")
    root, proof = tree([leaf(*x[:3]) for x in items])
    return {"round": rnd, "registry": catalog["registry"], "root": root.hex(),
            "message": message(rnd, catalog["registry"], root, magic).hex(), "passed": len(items),
            "leaves": [{"chainId": c, "address": a, "hash": h, "file": f, "proof": [p.hex() for p in proof(i)]}
                       for i, (c, a, h, f) in enumerate(items)]}


def latest():
    rs = sorted(ROUNDS.glob("*.json"), key=lambda p: int(p.stem)) if ROUNDS.exists() else []
    return rs[-1] if rs else None


def verify(r, pub_hex):
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.hazmat.primitives.asymmetric.utils import encode_dss_signature
    root = bytes.fromhex(r["root"])
    if bytes.fromhex(r["message"]) != message(r["round"], r["registry"], root, ADD if r.get("add") else MAGIC):
        return "message does not match round, registry and root"
    pub = ec.EllipticCurvePublicKey.from_encoded_point(ec.SECP256R1(), bytes.fromhex(pub_hex))
    sig = bytes.fromhex(r["signature"])
    try:
        pub.verify(encode_dss_signature(int.from_bytes(sig[:32], "big"), int.from_bytes(sig[32:], "big")),
                   bytes.fromhex(r["message"]), ec.ECDSA(hashes.SHA256()))
    except InvalidSignature:
        return "bad signature"
    for x in r["leaves"]:
        if fold(leaf(x["chainId"], x["address"], x["hash"]), [bytes.fromhex(p) for p in x["proof"]]) != root:
            return f"bad proof for {x['chainId']}:{x['address']}"
    return None


def pick(catalog, reviews, wanted):
    """The catalog cut down to the wanted descriptors (by file or hash); each must exist and have passed."""
    out = []
    for w in wanted:
        ds = [d for d in catalog["descriptors"] if w in (d["hash"], d["file"]) or d["file"].endswith("/" + w)]
        if len(ds) != 1:
            sys.exit(f"{w}: {len(ds)} descriptors match")
        f = reviews / f"{ds[0]['hash']}.json"
        result = json.loads(f.read_text())["result"] if f.exists() else "not reviewed"
        if result != "pass":
            sys.exit(f"{w}: {result}")
        out += ds
    return {**catalog, "descriptors": out}


def sign(r):
    r["signature"] = subprocess.run([str(ROOT / "se/clear-review-signer"), "sign", str(KEY), r["message"]], check=True, capture_output=True, text=True).stdout.strip()
    err = verify(r, PUB.read_text().strip())     # a wallet uses the key built into it, never one from the file
    if err:
        sys.exit("not written: " + err)
    return {k: r[k] for k in ("add", "round", "registry", "root", "message", "signature", "passed", "leaves") if k in r}


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "keygen":
        KEY.parent.mkdir(parents=True, exist_ok=True)
        pub = subprocess.run([str(ROOT / "se/clear-review-signer"), "create", str(KEY)], check=True, capture_output=True, text=True).stdout.strip()
        PUB.write_text(pub + "\n")
        print("clear-review.pub:", pub)
    elif cmd == "round":
        last = latest()
        rnd = int(last.stem) + 1 if last else 1
        r = sign(build(json.loads((ROOT / "work/catalog.json").read_text()), ROOT / "reviews", rnd))
        ROUNDS.mkdir(exist_ok=True)
        (ROUNDS / f"{rnd}.json").write_text(json.dumps(r, indent=1) + "\n")
        print(f"round {rnd}: {r['passed']} deployments, root {r['root'][:16]}…, registry {r['registry'][:7]}")
    elif cmd == "add":
        last = latest()
        if not last or len(sys.argv) < 3:
            sys.exit("needs a round first, and at least one descriptor")
        rnd = int(last.stem)
        k = len(list(ADDS.glob(f"{rnd}-*.json"))) + 1 if ADDS.exists() else 1
        cat = pick(json.loads((ROOT / "work/catalog.json").read_text()), ROOT / "reviews", sys.argv[2:])
        r = sign({"add": k, **build(cat, ROOT / "reviews", rnd, ADD)})
        ADDS.mkdir(exist_ok=True)
        (ADDS / f"{rnd}-{k}.json").write_text(json.dumps(r, indent=1) + "\n")
        print(f"add {rnd}-{k}: {r['passed']} deployments, root {r['root'][:16]}…")
    elif cmd == "verify":
        f = Path(sys.argv[2]) if len(sys.argv) > 2 else latest()
        r = json.loads(f.read_text())
        err = verify(r, PUB.read_text().strip())
        print((f"add {r['round']}-{r['add']}: " if r.get("add") else f"round {r['round']}: ") + (err or f"ok, {r['passed']} proofs"))
        sys.exit(1 if err else 0)
    else:
        print(open(__file__).read().split("\nimport ")[0])


if __name__ == "__main__":
    main()
