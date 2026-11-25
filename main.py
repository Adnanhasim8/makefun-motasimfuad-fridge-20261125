"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note from a smart fridge to its owner:
a single line, dry, petty and specific, to /output/entry.txt.

Python 3.13 standard library only. No network at run time.
"""

import os

ENTRY = (
    "I counted 14 door openings last night. "
    "The ice cream didn't move once. "
    "You were just... looking."
)


def main() -> None:
    # Gate assertions: the entry must be exactly one line, 1-200
    # characters, non-empty and not only whitespace.
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, (
        "entry must be a single line"
    )
    assert 1 <= len(ENTRY) <= 200, (
        f"entry must be 1-200 characters, got {len(ENTRY)}"
    )

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Verify what was actually written matches the gate too.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written output differs from entry"
    assert written.count("\n") == 0, "output must be exactly one line"
    assert 1 <= len(written) <= 200, "written output must be 1-200 chars"


if __name__ == "__main__":
    main()
