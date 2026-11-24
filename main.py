#!/usr/bin/env python3
"""Two Lines to Your Past Self - make.fun bounty entry.

Writes one two-line warning to /output/entry.txt.
Line 1 warns the past self about one specific moment in a single
sentence; line 2 says in one sentence why that moment mattered and
what changed because of it. Stdlib only, no network, no environment
reads, deterministic.
"""
import os
import sys

ENTRY = (
    "Don't delete the voicemail your father left on 12 April, "
    "the one where he says he's proud of you.\n"
    "After his funeral you will replay it a hundred times, "
    "and it is the only recording of his voice you will ever have."
)

MAX_CHARS = 280
SENTENCE_ENDS = (".", "!", "?")


def fail(message):
    print(f"invalid entry: {message}", file=sys.stderr)
    return 1


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        return fail("entry is empty")
    if len(text) > MAX_CHARS:
        return fail(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    lines = text.split("\n")
    if len(lines) != 2:
        return fail(f"entry must be exactly 2 lines, got {len(lines)}")
    for line in lines:
        if not line.strip():
            return fail("entry has an empty line")
        # Each line must be exactly one sentence: one sentence-ending
        # mark, at the very end of the line.
        ends = sum(line.count(mark) for mark in SENTENCE_ENDS)
        if ends != 1 or not line.rstrip().endswith(SENTENCE_ENDS):
            return fail(f"line is not a single sentence: {line!r}")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != text:
            return fail("written file does not match the entry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
