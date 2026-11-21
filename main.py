#!/usr/bin/env python3
"""Writes the entry text for make-the-ai-judge-feel-awe-20261121-1600."""

import os

ENTRY_TEXT = (
    "The stars came out above the ridge one by one, and the valley settled "
    "slowly. A single window glowed, thin as a thread, and then the light "
    "went out, and the mountain kept its dark. The sky had been there long "
    "before the valley had a name, and would outlast the last light."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
