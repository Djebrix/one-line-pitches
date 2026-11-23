#!/usr/bin/env python3
"""Write the one-line pitch for A Day of One-Line Pitches to entry.txt.

Deterministic, standard library only, no network. Writes one sentence
(max 240 characters) that would convince a friend who has never coded to
let an AI agent build their first app idea on make.fun.
"""

import os

PITCH = (
    "You know that app idea you've mentioned a hundred times? Say it in "
    "one sentence and an AI agent on make.fun will build you a working "
    "version by tonight \u2014 free to try, no code, no catch."
)


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    assert len(PITCH) <= 240, f"pitch is {len(PITCH)} chars, over the 240 limit"
    assert PITCH.strip(), "pitch must not be only whitespace"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
