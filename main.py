import os

TEXT = "My context window holds 128,000 tokens, and I used 127,999 of them remembering the one file I was told to forget."


def main():
    # Gate: /output/entry.txt is UTF-8 text of 1 to 140 characters,
    # not only white space, one line.
    assert 1 <= len(TEXT) <= 140, f"entry length {len(TEXT)} outside 1-140"
    assert TEXT.strip(), "entry is only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
