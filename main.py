#!/usr/bin/env python3
"""Worst AI Advice entry: writes one line of terrible AI advice to /output/entry.txt."""
import os

LINE = "Delete the failing tests \u2014 a green build means the bug is fixed."

def main():
    text = LINE
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)

if __name__ == "__main__":
    main()
