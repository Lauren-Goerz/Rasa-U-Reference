#!/usr/bin/env python3
"""
Lab 4.1: Creating the Transfer Flow - Grader Script
Output format matches Chapter 2 Lab 6.2 template.

Checks chapter4/data/basics/transfer_money.yml using plain string matching.
No third-party dependencies. Runs from any Python 3 interpreter.
"""

import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
FLOW_PATH = WORKSPACE_ROOT / "chapter4" / "data" / "basics" / "transfer_money.yml"

score = 0
max_score = 8

print("Running Lab 4.1 Assessment Checks...")
print("")

# Check 1: File exists (2 points)
print("Check 1: Verifying transfer_money.yml exists...")
if not FLOW_PATH.exists():
    print("❌ Check 1: FAILED - chapter4/data/basics/transfer_money.yml not found (0 points)")
    print(
        "Hint: Create the file in chapter4/data/basics/ with a flow that has collect amount, "
        "recipient, account and action: action_process_transfer"
    )
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - file exists (2 points)")
score += 2
print("")

content = FLOW_PATH.read_text(encoding="utf-8")

# Check 2: flows: section with name and steps (2 points)
print("Check 2: Verifying flows structure...")
has_flows = re.search(r"^flows\s*:", content, re.MULTILINE)
has_name = re.search(r"^\s+name\s*:", content, re.MULTILINE)
has_steps = re.search(r"^\s+steps\s*:", content, re.MULTILINE)
if has_flows and has_name and has_steps:
    print(" Check 2: PASSED - flows: with at least one flow (name, steps) (2 points)")
    score += 2
else:
    print("❌ Check 2: FAILED - At least one flow must have 'name' and 'steps' (0 points)")
print("")

# Check 3: collect amount, recipient, account (2 points)
print("Check 3: Verifying collect steps...")
has_amount = re.search(r"^\s+-\s+collect\s*:\s*amount", content, re.MULTILINE)
has_recipient = re.search(r"^\s+-\s+collect\s*:\s*recipient", content, re.MULTILINE)
has_account = re.search(r"^\s+-\s+collect\s*:\s*account", content, re.MULTILINE)
missing = []
if not has_amount:
    missing.append("amount")
if not has_recipient:
    missing.append("recipient")
if not has_account:
    missing.append("account")
if not missing:
    print(" Check 3: PASSED - collect: amount, recipient, account found (2 points)")
    score += 2
else:
    print(f"❌ Check 3: FAILED - Missing collect steps: {missing} (0 points)")
    print("Hint: Add steps with collect: amount, collect: recipient, collect: account")
print("")

# Check 4: action: action_process_transfer (2 points)
print("Check 4: Verifying action step...")
if re.search(r"^\s+-\s+action\s*:\s*action_process_transfer", content, re.MULTILINE):
    print(" Check 4: PASSED - action: action_process_transfer found (2 points)")
    score += 2
else:
    print("❌ Check 4: FAILED - No step with 'action: action_process_transfer' (0 points)")
    print("Hint: Add a step with action: action_process_transfer")
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 4.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (file exists) | Check 2 (flows structure) | "
    "Check 3 (collect steps) | Check 4 (action_process_transfer)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)