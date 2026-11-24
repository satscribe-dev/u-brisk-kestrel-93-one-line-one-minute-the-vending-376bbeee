#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single vending-machine pickup line (<=200 chars) to /output/entry.txt.
Deterministic, no network, no secrets, no input files.
"""
import os

ENTRY = "My coil's been stuck on you all week. One press of B7 and I'll finally let go \u2014 of the chocolate, I mean. Mostly."

def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
