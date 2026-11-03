#!/usr/bin/env python3
"""
Lab 4.1: Creating a Flow with Slot Collection - Grader Script
Checks chapter3/data/basics/check_balance.yml using plain string matching.
No third-party dependencies. Runs from any Python 3 interpreter.
"""

import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
FLOW_PATH = WORKSPACE_ROOT / "chapter3" / "data" / "basics" / "check_balance.yml"

score = 0
max_score = 8

print("Running Lab 4.1 Assessment Checks...")
print("")

# Check 1: File exists (2 points)
print("Check 1: Verifying check_balance.yml exists...")
if not FLOW_PATH.exists():
    print("❌ Check 1: FAILED - chapter3/data/basics/check_balance.yml not found (0 points)")
    print("Hint: Create the file at chapter3/data/basics/check_balance.yml.")
    sys.exit(1)
print(" Check 1: PASSED - file exists (2 points)")
score += 2
print("")

content = FLOW_PATH.read_text(encoding="utf-8")

# Check 2: flows: section with check_balance id and description (2 points)
print("Check 2: Verifying flows: section and check_balance flow...")
has_flows = re.search(r"^flows\s*:", content, re.MULTILINE)
has_flow_id = re.search(r"^\s{2}check_balance\s*:", content, re.MULTILINE)
has_description = re.search(r"^\s+description\s*:", content, re.MULTILINE)
if not has_flows:
    print("❌ Check 2: FAILED - No top-level flows: section found (0 points)")
    print("Hint: Add a flows: section at the top level of check_balance.yml.")
elif not has_flow_id:
    print("❌ Check 2: FAILED - No flow with id 'check_balance' found (0 points)")
    print("Hint: Add 'check_balance:' as a flow id under flows:.")
elif not has_description:
    print("⚠️  Check 2: PARTIAL - check_balance flow found but description: is missing (1 point)")
    score += 1
else:
    print(" Check 2: PASSED - check_balance flow with description (2 points)")
    score += 2
print("")

# Check 3: collect: account step (2 points)
print("Check 3: Verifying collect: account step...")
if re.search(r"^\s+-\s+collect\s*:\s*account", content, re.MULTILINE):
    print(" Check 3: PASSED - collect: account found in steps (2 points)")
    score += 2
else:
    print("❌ Check 3: FAILED - No collect: account step found (0 points)")
    print("Hint: Add '- collect: account' under steps:.")
print("")

# Check 4: action: action_check_balance_simple step (2 points)
print("Check 4: Verifying action: action_check_balance_simple step...")
if re.search(r"^\s+-\s+action\s*:\s*action_check_balance_simple", content, re.MULTILINE):
    print(" Check 4: PASSED - action: action_check_balance_simple found (2 points)")
    score += 2
else:
    print("❌ Check 4: FAILED - No action: action_check_balance_simple step found (0 points)")
    print("Hint: Add '- action: action_check_balance_simple' after the collect step.")
print("")

print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 4.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (file) | Check 2 (flows + check_balance flow) | "
    "Check 3 (collect: account) | Check 4 (action: action_check_balance_simple)"
)
print(f"Score: {score}/{max_score}")

sys.exit(0 if score >= max_score else 1)