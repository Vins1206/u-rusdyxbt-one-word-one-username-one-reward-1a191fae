"""One Word, One Username, One Reward.

Entry for make.fun competition
u-rusdyxbt-one-word-one-username-one-reward-1a191fae.

The program writes the entrant's own make.fun username, one word
and nothing else, to /output/entry.txt, then stops. No input file
is read: this competition ships no dataset (input_data is null),
so the entry is the handle itself.

Username: vins12 (6 characters, one word, no spaces, no newline).
Pure standard library, deterministic: every run writes the same
bytes.
"""

USERNAME = "vins12"
OUTPUT_PATH = "/output/entry.txt"

import os


def main() -> None:
    # Enforce the gate before writing: 1-30 chars, a single word,
    # no spaces, no newline, not only whitespace.
    assert 1 <= len(USERNAME) <= 30
    assert USERNAME == USERNAME.strip()
    assert " " not in USERNAME and "\n" not in USERNAME
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
