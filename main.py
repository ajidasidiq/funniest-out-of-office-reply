#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes one out-of-office auto-reply line to /output/entry.txt.
The entry is the line itself: a fixed string, no generation, no
network, no environment input, so every run writes identical bytes.
"""

from __future__ import annotations

import hashlib
import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160

ENTRY_LINE = (
    "I'm away until Monday. "
    "Your email is important to me, "
    "which is why I've arranged for nobody to read it."
)


def main() -> int:
    if not 1 <= len(ENTRY_LINE) <= MAX_CHARS:
        raise SystemExit("entry line fails the 1-160 character gate")
    if ENTRY_LINE != ENTRY_LINE.strip() or "\n" in ENTRY_LINE:
        raise SystemExit("entry line must be a single clean line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_LINE)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != ENTRY_LINE.encode("utf-8"):
        raise SystemExit("post-write check: entry.txt is not the entry line")
    print("entry md5:", hashlib.md5(written).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
