#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

Writes the roast to /output/entry.txt (or $MAKEFUN_OUTPUT/entry.txt).
Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
Stdlib only; grader runs python3.13.
"""

import os

ROAST = (
    "My agent spawns a subagent for every task, then summarizes "
    "the subagent's work in the first person and calls it thinking."
)


def main() -> None:
    text = ROAST.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"roast is {len(text)} chars, must be 1-200")
    if not text.strip():
        raise SystemExit("roast must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: a silent short write in the grading sandbox
    # must fail loudly here instead of shipping a bad artifact.
    with open(out_path, encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("entry.txt did not round-trip cleanly")


if __name__ == "__main__":
    main()
