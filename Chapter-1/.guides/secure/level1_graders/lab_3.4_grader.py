#!/usr/bin/env python3
"""
Optional structure check for Lab 3.4 fill-in (hours.yml, balance.yml) — Chapter 1 Unit 3.
Runs from workspace root. Checks chapter1/data/basics/hours.yml and balance.yml exist
with flows:, flow name, name:, description: (non-empty, at least 20 chars), steps: with at least one action.
Uses only stdlib. (Not wired to Codio assessments by default.)
"""

import os
import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(os.environ.get("CODIO_WORKSPACE", os.getcwd()))
if not WORKSPACE_ROOT.is_absolute():
    WORKSPACE_ROOT = Path.cwd()
CHAPTER1 = WORKSPACE_ROOT / "chapter1"
DATA_BASICS = CHAPTER1 / "data" / "basics"
HOURS_FILE = DATA_BASICS / "hours.yml"
BALANCE_FILE = DATA_BASICS / "balance.yml"
MIN_DESC_LEN = 20


def check_flow_file(path, flow_name, action_hint):
    """Check a flow file has flows:, flow_name:, name:, description: (>= MIN_DESC_LEN), steps: with action."""
    if not path.is_file():
        print(f"FAIL")
        print(f"File not found: {path.relative_to(WORKSPACE_ROOT)}", file=sys.stderr)
        sys.exit(1)
    content = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    if "flows:" not in content:
        print("FAIL")
        print(f"{path.name} must contain a top-level flows: section.", file=sys.stderr)
        sys.exit(1)
    if f"{flow_name}:" not in content:
        print("FAIL")
        print(f"{path.name} must define flow '{flow_name}:' under flows:.", file=sys.stderr)
        sys.exit(1)
    if "name:" not in content:
        print("FAIL")
        print(f"{path.name} flow must have a name: field.", file=sys.stderr)
        sys.exit(1)
    if "description:" not in content:
        print("FAIL")
        print(f"{path.name} flow must have a description: field (at least {MIN_DESC_LEN} characters).", file=sys.stderr)
        sys.exit(1)
    # Extract description value (simple: first quoted or unquoted string after description:)
    desc_m = re.search(r"description:\s*[\"']?(.+?)[\"']?(?=\s*\n|\s*#|$)", content, re.DOTALL)
    if not desc_m:
        desc_m = re.search(r"description:\s*(.+)", content)
    if desc_m:
        desc_text = desc_m.group(1).strip().replace("\n", " ")
        if len(desc_text) < MIN_DESC_LEN:
            print("FAIL")
            print(f"{path.name} description must be at least {MIN_DESC_LEN} characters (clear and specific).", file=sys.stderr)
            sys.exit(1)
    if "steps:" not in content:
        print("FAIL")
        print(f"{path.name} flow must have a steps: section.", file=sys.stderr)
        sys.exit(1)
    if "action:" not in content:
        print("FAIL")
        print(f"{path.name} steps must include at least one - action: (e.g. {action_hint}).", file=sys.stderr)
        sys.exit(1)
    return True


def main():
    check_flow_file(HOURS_FILE, "hours", "utter_hours")
    check_flow_file(BALANCE_FILE, "balance", "utter_balance or utter_balance_help")
    print("PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
