import os
import struct
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_BYTES = 1024 * 1024
MAX_DIM = 1024


def png_dims(path):
    with open(path, "rb") as f:
        head = f.read(24)
    assert head[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
    w, h = struct.unpack(">II", head[16:24])
    return w, h


def test_entry():
    with tempfile.TemporaryDirectory() as tmp:
        env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
        r = subprocess.run(
            [sys.executable, os.path.join(HERE, "main.py")],
            env=env, capture_output=True, text=True, timeout=60,
        )
        assert r.returncode == 0, r.stderr
        out = os.path.join(tmp, "entry.png")
        size = os.path.getsize(out)
        assert size <= MAX_BYTES, f"entry.png is {size} bytes, over {MAX_BYTES}"
        w, h = png_dims(out)
        assert w <= MAX_DIM and h <= MAX_DIM, f"dims {w}x{h} over {MAX_DIM}"
        with open(os.path.join(HERE, "entry.png"), "rb") as a, open(out, "rb") as b:
            assert a.read() == b.read(), "output must be a byte-identical copy"
        print(f"ok: entry.png {w}x{h}, {size} bytes")


if __name__ == "__main__":
    test_entry()
