"""Vending machine pickup line writer.

Reads the entry line from entry.txt next to this file and writes it to
/output/entry.txt as UTF-8 text, mode 0644, so the grader can read it.
Stdlib only, no network, deterministic.
"""

import os
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    entry_path = here / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 and ch not in "\n\t" for ch in text):
        print("entry contains control characters", file=sys.stderr)
        return 1
    if len(text) > 200:
        print("entry is over 200 characters", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text + "\n", encoding="utf-8")
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
