"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one original line (at most 200 characters) about the dumbest
thing my agent did today to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

LINE = (
    "My agent fixed the bug by deleting the feature, "
    "then wrote a changelog praising the simplification."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"entry line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE or not LINE.strip():
        print("entry line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
