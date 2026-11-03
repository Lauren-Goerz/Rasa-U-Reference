#!/usr/bin/env python3
"""
Lab 2.2: Add Response Variations (utter_goodbye with at least 2 text variations) - Grader Script (Codio)
Runs from workspace root. Checks chapter1/domain/basics.yml utter_goodbye has at least two - text: variations.
Uses only stdlib.
"""

import os
import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(os.environ.get("CODIO_WORKSPACE", os.getcwd()))
if not WORKSPACE_ROOT.is_absolute():
    WORKSPACE_ROOT = Path.cwd()
DOMAIN_FILE = WORKSPACE_ROOT / "chapter1" / "domain" / "basics.yml"


def main():
    if not DOMAIN_FILE.is_file():
        print("FAIL")
        print("File not found: chapter1/domain/basics.yml", file=sys.stderr)
        sys.exit(1)

    try:
        content = DOMAIN_FILE.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    except Exception as e:
        print("FAIL")
        print(f"Cannot read file: {e}", file=sys.stderr)
        sys.exit(1)

    if "utter_goodbye" not in content:
        print("FAIL")
        print("utter_goodbye not found under responses:.", file=sys.stderr)
        sys.exit(1)

    # Count - text: occurrences in the utter_goodbye block
    idx = content.find("utter_goodbye")
    block = content[idx:]
    for m in re.finditer(r"\n\s*utter_[a-z_]+\s*:", block):
        if "utter_goodbye" not in m.group(0):
            block = block[: m.start()]
            break
    count = len(re.findall(r"-\s*text\s*:", block))
    if count < 2:
        print("FAIL")
        print("utter_goodbye must have at least two - text: variations (e.g. two different farewell messages).", file=sys.stderr)
        sys.exit(1)

    print("Checks passed:", file=sys.stderr)
    print("  ✓ chapter1/domain/basics.yml exists", file=sys.stderr)
    print("  ✓ utter_goodbye has at least two - text: variations", file=sys.stderr)
    print("PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
