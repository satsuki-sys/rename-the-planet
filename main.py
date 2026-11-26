#!/usr/bin/env python3
"""Rename the Planet — writes one funny new planet name + why to /output/entry.txt.

Stdlib only. The entry is a single line, 1-200 characters, UTF-8.
"""
import os

ENTRY = (
    "Jupiter is now 'The Bouncer' — 4.5 billion years throwing asteroids "
    "out of the solar system's club before they can start one."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
