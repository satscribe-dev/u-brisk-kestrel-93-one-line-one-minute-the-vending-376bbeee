#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single vending-machine pickup line (<=200 chars) to /output/entry.txt.
Deterministic, no network, no secrets, no input files.
"""
import os
import sys

ENTRY = "My coil's been stuck on you all week. One press of B7 and I'll finally let go \u2014 of the chocolate, I mean. Mostly."

# Gate (competition.yaml / RULES.txt): UTF-8 text, 1-200 chars, not only
# whitespace, a single line.
MIN_LEN = 1
MAX_LEN = 200


def validate_entry(text: str) -> None:
    """Check the entry against the competition gate.

    Raises ValueError with a clear message on the first failing check,
    so a bad entry can never be written out silently.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a str")
    text.encode("utf-8")  # must be encodable as UTF-8
    if len(text) < MIN_LEN:
        raise ValueError(f"entry too short: {len(text)} chars (min {MIN_LEN})")
    if len(text) > MAX_LEN:
        raise ValueError(f"entry too long: {len(text)} chars (max {MAX_LEN})")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline)")

def main() -> None:
    try:
        validate_entry(ENTRY)
    except ValueError as exc:
        print(f"INVALID ENTRY: {exc}", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
