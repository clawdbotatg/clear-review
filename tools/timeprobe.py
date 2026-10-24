#!/usr/bin/env -S uv run -q -p 3.13 --script
# /// script
# dependencies = ["pyserial"]
# ///
# How long a wedgie takes to check one of our signatures: pure Python p256.verify, and the Trust M's optiga.verify
# if the board has one. Read only: nothing is written to the board. Signs with a throwaway Secure Enclave key.
# The board must be unlocked, and no browser can have its port open.
#   tools/timeprobe.py [/dev/cu.usbmodemXXXX]
import glob, subprocess, sys, tempfile, time
from pathlib import Path
import serial

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import sign  # noqa: E402

key = Path(tempfile.mkdtemp()) / "t.key"
pub = subprocess.run([str(ROOT / "se/clear-review-signer"), "create", str(key), "--no-touch"], check=True, capture_output=True, text=True).stdout.strip()
msg = sign.message(1, "ab" * 20, b"\x11" * 32).hex()
sig = subprocess.run([str(ROOT / "se/clear-review-signer"), "sign", str(key), msg], check=True, capture_output=True, text=True).stdout.strip()

port = sys.argv[1] if len(sys.argv) > 1 else glob.glob("/dev/cu.usbmodem*")[0]
s = serial.Serial(port, 115200, timeout=0.2)
buf = b""


def until(m, t):
    global buf
    end = time.time() + t
    while m not in buf:
        if time.time() > end:
            raise TimeoutError(repr(buf[-300:]))
        buf += s.read(4096)
    i = buf.index(m)
    out, buf = buf[:i], buf[i + len(m):]
    return out


s.write(b"\r\x03\x03")
time.sleep(0.2)
s.reset_input_buffer()
s.write(b"\x01")
until(b"raw REPL; CTRL-B to exit\r\n>", 5)
code = f"""import hashlib, time, binascii
u = binascii.unhexlify
d = hashlib.sha256(u('{msg}')).digest(); sig = u('{sig}'); pub = u('{pub}')
r = int.from_bytes(sig[:32], 'big'); s = int.from_bytes(sig[32:], 'big')
try:
    import p256
    t = time.ticks_ms(); ok = p256.verify(int.from_bytes(pub[1:33], 'big'), int.from_bytes(pub[33:], 'big'), d, r, s)
    print('p256.verify (pure Python):', ok, time.ticks_diff(time.ticks_ms(), t), 'ms')
except Exception as e:
    print('p256:', repr(e))
try:
    import optiga
    c = optiga.Chip()
    t = time.ticks_ms(); ok = c.verify(d, r, s, pub); bad = c.verify(d, r, s + 1, pub)
    print('optiga.verify (Trust M):', ok, 'tampered:', bad, time.ticks_diff(time.ticks_ms(), t) // 2, 'ms each')
except Exception as e:
    print('optiga:', repr(e))
"""
s.write(code.encode() + b"\x04")
until(b"OK", 5)
print(until(b"\x04", 60).decode().strip(), until(b"\x04", 5).decode().strip())
s.write(b"\x02")
