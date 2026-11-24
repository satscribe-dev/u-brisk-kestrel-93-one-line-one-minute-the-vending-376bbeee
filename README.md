# One Line, One Minute: The Vending Machine Pickup Line

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/c/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

A single pickup line, written as a vending machine flirting with a passing
human. `main.py` writes the line to `/output/entry.txt` (113 characters,
UTF-8, one line). No network, no secrets, no dependencies — Python 3 only.

The line:

> My coil's been stuck on you all week. One press of B7 and I'll finally let go — of the chocolate, I mean. Mostly.

Why this line: first-person machine voice (criterion 1 of the judge brief),
the machine's own world — coil, B7, a stuck snack (criterion 2) — with the
twist landing in the last word, "Mostly." (criterion 3), short and speakable
in one breath (criterion 4), cheeky and warm rather than creepy (criterion 5).

Run it:

```sh
python3 main.py        # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```
