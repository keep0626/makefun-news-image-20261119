#!/usr/bin/env python3
"""make.fun bounty: Sum up 19 November's world news in one image.
Deterministic, offline: copies the pre-built entry.png to /output/entry.png.
No network, no randomness, no model calls.
The image itself is built by build_image.py (PIL, DejaVu Sans) from the
six verified 19 Nov 2026 stories listed in README.md.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main() -> int:
    if not os.path.isfile(SRC):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
