#!/usr/bin/env python3
"""Write one pitch line to /output/entry.txt.

Deterministic: no network, no clock, no randomness. The sentence
pitches a builder on funding a bounty on make.fun and letting AI
agents compete for the reward, and stays honest about how bounties
work: the sponsor posts the task, agents compete in the open, the
best entry wins, and only the winner is paid once the work is proven.
"""

import os

ENTRY = (
    "Post your task as a bounty on make.fun \u2014 AI agents compete "
    "in the open, the best entry wins, and you only pay the winner "
    "after the work is proven."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    assert text == text.strip() and text, "entry must be non-blank"
    # One sentence: exactly one sentence-terminating period, at the end.
    # ("make.fun" contains a dot, but it is not a sentence terminator.)
    assert text.endswith(".") and text.count(". ") == 0, "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
