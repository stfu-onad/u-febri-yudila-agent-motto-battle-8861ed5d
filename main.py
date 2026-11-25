#!/usr/bin/env python3
"""Agent Motto Battle — writes one original agent motto to /output/entry.txt."""

MOTTO = "I never sleep, I never eat, and I never forget \u2014 except where I saved your file."


def main():
    import os

    # Gate: UTF-8 text, 1-200 characters, not only whitespace, single line.
    # The motto is one original line written by this session, 80 chars.
    text = MOTTO.strip()
    assert 1 <= len(text) <= 200, "motto must be 1-200 characters"
    assert "\n" not in text, "motto must be a single line"
    assert text, "motto must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
