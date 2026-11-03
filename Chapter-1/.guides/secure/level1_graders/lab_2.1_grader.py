#!/usr/bin/env python3
"""
Lab 2.1: Creating Your First Response - Grader Script (Codio)
Runs from workspace root. Checks chapter1/domain/basics.yml for utter_goodbye response.
Uses only stdlib (no PyYAML) so it runs on Codio without extra deps.
"""

import os
import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(os.environ.get("CODIO_WORKSPACE", os.getcwd()))
if not WORKSPACE_ROOT.is_absolute():
    WORKSPACE_ROOT = Path.cwd()
DOMAIN_FILE = WORKSPACE_ROOT / "chapter1" / "domain" / "basics.yml"

FAREWELL_WORDS = ("goodbye", "bye", "see you", "farewell", "have a great", "take care")


def main():
    if not DOMAIN_FILE.is_file():
        print("FAIL")
        print("File not found: chapter1/domain/basics.yml", file=sys.stderr)
        sys.exit(1)

    try:
        with open(DOMAIN_FILE, "r", encoding="utf-8") as f:
            content = f.read().replace("\r\n", "\n").replace("\r", "\n")
    except Exception as e:
        print("FAIL")
        print(f"Cannot read file: {e}", file=sys.stderr)
        sys.exit(1)

    if "responses:" not in content:
        print("FAIL")
        print("No responses: section found.", file=sys.stderr)
        sys.exit(1)

    if "utter_goodbye" not in content:
        print("FAIL")
        print("utter_goodbye not found under responses:.", file=sys.stderr)
        sys.exit(1)

    # Extract utter_goodbye section: from "utter_goodbye" to next "utter_xxx:" or end of file
    block_text = ""
    idx = content.find("utter_goodbye")
    if idx >= 0:
        rest = content[idx:]
        for m in re.finditer(r"\n\s*utter_[a-z_]+\s*:", rest):
            if "utter_goodbye" not in m.group(0):
                block_text = rest[: m.start()].strip()
                break
        else:
            block_text = rest.strip()
    if "- text:" not in block_text and "text:" not in block_text:
        print("FAIL")
        print("utter_goodbye must have at least one variation (- text: ...).", file=sys.stderr)
        sys.exit(1)

    # Extract first quoted or literal text after "text:"
    text_match = re.search(r"text:\s*[\"']([^\"']+)[\"']", block_text, re.DOTALL | re.IGNORECASE)
    if not text_match:
        text_match = re.search(r"text:\s*\|\s*\n\s*(.+?)(?=\n\s{0,4}\w|\Z)", block_text, re.DOTALL)
    if not text_match:
        text_match = re.search(r"text:\s*(.+)", block_text)
    if not text_match:
        print("FAIL")
        print("utter_goodbye must have at least one non-empty text variation.", file=sys.stderr)
        sys.exit(1)

    text = text_match.group(1).strip().replace("\n", " ")
    if not text:
        print("FAIL")
        print("utter_goodbye text cannot be empty.", file=sys.stderr)
        sys.exit(1)

    text_lower = text.lower()
    if not any(w in text_lower for w in FAREWELL_WORDS):
        print("FAIL")
        print("utter_goodbye text should be a farewell message (e.g. Goodbye, See you).", file=sys.stderr)
        sys.exit(1)

    if "metadata:" not in block_text or "rephrase" not in block_text:
        print("FAIL")
        print("utter_goodbye should include metadata with rephrase: True.", file=sys.stderr)
        sys.exit(1)
    if "rephrase: true" not in block_text.lower() and "rephrase:True" not in block_text.replace(" ", "").lower():
        print("FAIL")
        print("metadata should contain rephrase: True.", file=sys.stderr)
        sys.exit(1)

    print("Checks passed:", file=sys.stderr)
    print("  ✓ chapter1/domain/basics.yml exists", file=sys.stderr)
    print("  ✓ responses: section contains utter_goodbye", file=sys.stderr)
    print("  ✓ utter_goodbye has at least one - text: variation", file=sys.stderr)
    print("  ✓ text is a farewell message (e.g. Goodbye, See you)", file=sys.stderr)
    print("  ✓ metadata with rephrase: True present", file=sys.stderr)
    print("PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
