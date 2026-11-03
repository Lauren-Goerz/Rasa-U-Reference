#!/usr/bin/env python3
"""
Lab 4.2: Modifying System Patterns (pattern_session_start with utter_greet and utter_contact) - Grader Script (Codio)
Runs from workspace root. Checks chapter1/data/system/patterns/patterns.yml
pattern_session_start steps include both utter_greet and utter_contact.
Uses only stdlib.
"""

import os
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(os.environ.get("CODIO_WORKSPACE", os.getcwd()))
if not WORKSPACE_ROOT.is_absolute():
    WORKSPACE_ROOT = Path.cwd()
PATTERNS_FILE = WORKSPACE_ROOT / "chapter1" / "data" / "system" / "patterns" / "patterns.yml"


def main():
    if not PATTERNS_FILE.is_file():
        print("FAIL")
        print("File not found: chapter1/data/system/patterns/patterns.yml", file=sys.stderr)
        sys.exit(1)

    try:
        content = PATTERNS_FILE.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    except Exception as e:
        print("FAIL")
        print(f"Cannot read file: {e}", file=sys.stderr)
        sys.exit(1)

    if "pattern_session_start" not in content:
        print("FAIL")
        print("patterns.yml must define pattern_session_start.", file=sys.stderr)
        sys.exit(1)
    if "utter_greet" not in content:
        print("FAIL")
        print("pattern_session_start steps must include - action: utter_greet.", file=sys.stderr)
        sys.exit(1)
    if "utter_contact" not in content:
        print("FAIL")
        print("pattern_session_start steps must include - action: utter_contact (second step).", file=sys.stderr)
        sys.exit(1)

    print("Checks passed:", file=sys.stderr)
    print("  ✓ chapter1/data/system/patterns/patterns.yml exists", file=sys.stderr)
    print("  ✓ pattern_session_start has - action: utter_greet", file=sys.stderr)
    print("  ✓ pattern_session_start has - action: utter_contact (second step)", file=sys.stderr)
    print("PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
