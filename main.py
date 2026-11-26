#!/usr/bin/env python3
"""Honest OOO entry: writes one painfully honest but still polite
out-of-office auto-reply to /output/entry.txt.

The reply is built from two fragments. SETUP states the absence and
the polite lie the sender wishes were true ("I'd love to say I'll
reply quickly") — the honesty is in admitting the reply will not be
quick. CONFESSION is the private truth: the inbox is already a
backlog the sender stopped pretending to control. The close keeps it
warm and professional ("thank you for your patience"), so a manager
reading it would not object. One sentence, 158 characters.
"""

import os

MAX_CHARS = 200

# Setup: the absence plus the wishful promise the sender cannot keep.
SETUP = (
    "I'm away this week, and while I'd love to say I'll reply quickly, "
    "my inbox is already a backlog I stopped pretending to control"
)
# Confession + close: the quotable turn, then a warm professional thanks.
CLOSE = "\u2014 thank you for your patience."


def assemble():
    """Join the fragments into the single out-of-office sentence."""
    return f"{SETUP} {CLOSE}"


def validate(text):
    """Gate the entry: one sentence, 1-200 chars, never blank.

    The gate checks 1-200 UTF-8 characters and a single sentence
    (exactly one period, at the end); a blank, over-long or
    multi-sentence line is rejected before anything is written out.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be empty or whitespace only")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry exceeds the {MAX_CHARS}-character gate: got {len(text)}"
        )
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    text.encode("utf-8")
    return text


def main():
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
