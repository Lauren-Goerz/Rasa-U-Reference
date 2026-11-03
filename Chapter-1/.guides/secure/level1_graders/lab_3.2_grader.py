#!/usr/bin/env python3
"""
Lab 3.2: Creating Your First Flow (goodbye.yml) - Grader Script (Codio)
Runs from workspace root. Checks chapter1/data/basics/goodbye.yml exists
with flows:, goodbye:, name:, description:, steps:, and - action: utter_goodbye.
Uses only stdlib.
"""

import os
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(os.environ.get("CODIO_WORKSPACE", os.getcwd()))
if not WORKSPACE_ROOT.is_absolute():
    WORKSPACE_ROOT = Path.cwd()
GOODBYE_FILE = WORKSPACE_ROOT / "chapter1" / "data" / "basics" / "goodbye.yml"


def main():
    if not GOODBYE_FILE.is_file():
        print("FAIL")
        print("File not found: chapter1/data/basics/goodbye.yml", file=sys.stderr)
        sys.exit(1)

    try:
        content = GOODBYE_FILE.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    except Exception as e:
        print("FAIL")
        print(f"Cannot read file: {e}", file=sys.stderr)
        sys.exit(1)

    if "flows:" not in content:
        print("FAIL")
        print("goodbye.yml must contain a top-level flows: section.", file=sys.stderr)
        sys.exit(1)
    if "goodbye:" not in content:
        print("FAIL")
        print("goodbye.yml must define a flow named goodbye: under flows:.", file=sys.stderr)
        sys.exit(1)
    if "name:" not in content:
        print("FAIL")
        print("The goodbye flow must have a name: field.", file=sys.stderr)
        sys.exit(1)
    if "description:" not in content:
        print("FAIL")
        print("The goodbye flow must have a description: field (critical for LLM matching).", file=sys.stderr)
        sys.exit(1)
    if "steps:" not in content:
        print("FAIL")
        print("The goodbye flow must have a steps: section.", file=sys.stderr)
        sys.exit(1)
    if "utter_goodbye" not in content:
        print("FAIL")
        print("The steps: section must include - action: utter_goodbye.", file=sys.stderr)
        sys.exit(1)

    print("Checks passed:", file=sys.stderr)
    print("  ✓ chapter1/data/basics/goodbye.yml exists", file=sys.stderr)
    print("  ✓ flows: section with goodbye: flow", file=sys.stderr)
    print("  ✓ name: and description: fields present", file=sys.stderr)
    print("  ✓ steps: includes - action: utter_goodbye", file=sys.stderr)
    print("PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
