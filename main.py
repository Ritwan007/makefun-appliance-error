"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line of at most 200 characters to /output/entry.txt:
the funniest honest error message an appliance could show.
"""

# The winning line, selected by pairwise self-judging of 36 candidates
# against the judge brief (honest fault, real twist, flat machine voice,
# economy). An oven whose temperature sensor has drifted, calmly
# confessing it has been misreporting for months.
ENTRY_LINE = (
    "ERROR: Temperature sensor drifting. "
    "I said 200 degrees. I meant 140. "
    "I have been lying for months."
)


def main() -> None:
    """Write the entry line to /output/entry.txt (UTF-8, one line)."""
    line = ENTRY_LINE.strip()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line.strip(), "entry must not be blank"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
