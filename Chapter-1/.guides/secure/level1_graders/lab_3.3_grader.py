#!/usr/bin/env python3
"""
Lab 3.3: Multi-Step Flow (greet.yml with two steps) - Grader Script (Codio)
Runs from workspace root. Checks chapter1/data/basics/greet.yml has
both - action: utter_greet and - action: utter_help in steps.
Uses only stdlib.
"""

import os
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(os.environ.get("CODIO_WORKSPACE", os.getcwd()))
if not WORKSPACE_ROOT.is_absolute():
    WORKSPACE_ROOT = Path.cwd()
GREET_FILE = WORKSPACE_ROOT / "chapter1" / "data" / "basics" / "greet.yml"


def main():
    if not GREET_FILE.is_file():
        print("FAIL")
        print("File not found: chapter1/data/basics/greet.yml", file=sys.stderr)
        sys.exit(1)

    try:
        content = GREET_FILE.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    except Exception as e:
        print("FAIL")
        print(f"Cannot read file: {e}", file=sys.stderr)
        sys.exit(1)

    if "utter_greet" not in content:
        print("FAIL")
        print("greet.yml steps must include - action: utter_greet.", file=sys.stderr)
        sys.exit(1)
    if "utter_help" not in content:
        print("FAIL")
        print("greet.yml steps must include - action: utter_help (second step).", file=sys.stderr)
        sys.exit(1)
    if "steps:" not in content:
        print("FAIL")
        print("greet.yml must have a steps: section.", file=sys.stderr)
        sys.exit(1)

    print("Checks passed:", file=sys.stderr)
    print("  ✓ chapter1/data/basics/greet.yml exists", file=sys.stderr)
    print("  ✓ steps: includes - action: utter_greet", file=sys.stderr)
    print("  ✓ steps: includes - action: utter_help (second step)", file=sys.stderr)
    print("PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
