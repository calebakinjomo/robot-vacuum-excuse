#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — a make.fun bounty entry.

Writes one line, at most 140 characters, to /output/entry.txt: the
funniest excuse a robot vacuum could give for missing a spot.

The excuse: a crumb that dodged three times wins the day — the vacuum
keeps its dignity and returns to its dock.
"""

import os

ENTRY = "That crumb dodged me three times, so I let it win. I have a dock to return to and dignity to keep."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
