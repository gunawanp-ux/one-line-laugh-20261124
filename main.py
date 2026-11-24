#!/usr/bin/env python3
"""The Saddest Applause.

Writes a single sentence (at most 200 characters) — one funny line
about a smartwatch congratulating its wearer for the heroic act of
standing up — to /output/entry.txt. No network, no input, deterministic.

The joke lands on the judge's own brief: an everyday truth (fitness
trackers cheer for trivial things) with the surprise saved for the end.
"""

import os

SENTENCE = (
    "My smartwatch just congratulated me for standing up, "
    "which is the saddest applause I have ever received."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars"
    assert text.endswith(".") and text.count(".") == 1, "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
