#!/usr/bin/env python3
"""One-line excuse: the excuse an AI agent gives its human for missing a deadline."""

import os

EXCUSE = "I delegated the deadline to a subagent. It delegated it back to me."

OUT_PATH = "/output/entry.txt"


def main():
    # The gate wants 1-160 characters, not only whitespace, on a single line.
    # The joke: the deadline bounced between the agent and its subagent in a
    # delegation loop, so nobody did it — an excuse only an agent could give.
    if not (1 <= len(EXCUSE) <= 160) or EXCUSE.isspace() or "\n" in EXCUSE:
        raise ValueError("entry must be one line of 1-160 characters, not only whitespace")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
