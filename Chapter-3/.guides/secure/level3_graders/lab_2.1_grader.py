#!/usr/bin/env python3
"""
Lab 2.1: Defining a Slot in the Domain - Grader Script
Checks chapter3/domain/basics.yml using plain string matching.
No third-party dependencies. Runs from any Python 3 interpreter.
"""

import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
DOMAIN_PATH = WORKSPACE_ROOT / "chapter3" / "domain" / "basics.yml"

score = 0
max_score = 11

print("Running Lab 2.1 Assessment Checks...")
print("")

# Check 1: Domain file exists
print("Check 1: Verifying domain file exists...")
if not DOMAIN_PATH.exists():
    print("❌ Check 1: FAILED - chapter3/domain/basics.yml not found (0 points)")
    print("Hint: Create domain/basics.yml inside the chapter3 folder.")
    sys.exit(1)
print(" Check 1: PASSED - chapter3/domain/basics.yml exists (1 point)")
score += 1
print("")

content = DOMAIN_PATH.read_text(encoding="utf-8")

# Check 2: slots: section present
print("Check 2: Verifying slots: section...")
if not re.search(r"^slots\s*:", content, re.MULTILINE):
    print("❌ Check 2: FAILED - No top-level slots: section found (0 points)")
    print("Hint: Add a slots: section at the top level of domain/basics.yml.")
else:
    print(" Check 2: PASSED - slots: section present (2 points)")
    score += 2
print("")

# Check 3: account slot with type text
print("Check 3: Verifying account slot...")
has_account = re.search(r"^\s{2}account\s*:", content, re.MULTILINE)
has_type_text = re.search(r"^\s+type\s*:\s*text", content, re.MULTILINE)
if not has_account:
    print("❌ Check 3: FAILED - account slot not found under slots: (0 points)")
    print("Hint: Add 'account:' under slots: with type: text and mappings: - type: from_llm")
elif not has_type_text:
    print("⚠️  Check 3: PARTIAL - account slot found but type: text missing (1 point)")
    score += 1
else:
    print(" Check 3: PASSED - account slot with type: text (2 points)")
    score += 2
print("")

# Check 4: utter_ask_account in responses
print("Check 4: Verifying utter_ask_account response...")
has_ask = re.search(r"^\s+utter_ask_account\s*:", content, re.MULTILINE)
has_ask_text = re.search(r"utter_ask_account[\s\S]{0,200}text\s*:", content)
if not has_ask:
    print("❌ Check 4: FAILED - utter_ask_account not found under responses: (0 points)")
    print("Hint: Add utter_ask_account with a text message under responses:.")
elif not has_ask_text:
    print("⚠️  Check 4: PARTIAL - utter_ask_account present but no text message found (1 point)")
    score += 1
else:
    print(" Check 4: PASSED - utter_ask_account with message (2 points)")
    score += 2
print("")

# Check 5: utter_invalid_account in responses
print("Check 5: Verifying utter_invalid_account response...")
if not re.search(r"^\s+utter_invalid_account\s*:", content, re.MULTILINE):
    print("❌ Check 5: FAILED - utter_invalid_account not found under responses: (0 points)")
    print("Hint: Add utter_invalid_account with a text message under responses:.")
else:
    print(" Check 5: PASSED - utter_invalid_account present (1 point)")
    score += 1
print("")

# Check 6: action_check_balance_simple in actions
print("Check 6: Verifying action_check_balance_simple in actions...")
if not re.search(r"^\s*-\s*action_check_balance_simple", content, re.MULTILINE):
    print("❌ Check 6: FAILED - action_check_balance_simple not found in actions: (0 points)")
    print("Hint: Add '- action_check_balance_simple' under the actions: section.")
else:
    print(" Check 6: PASSED - action_check_balance_simple registered (1 point)")
    score += 1
print("")

# Check 7: action_bank_hours in actions
print("Check 7: Verifying action_bank_hours in actions...")
if not re.search(r"^\s*-\s*action_bank_hours", content, re.MULTILINE):
    print("❌ Check 7: FAILED - action_bank_hours missing from actions: (0 points)")
    print("Hint: Add '- action_bank_hours' under the actions: section.")
else:
    print(" Check 7: PASSED - action_bank_hours present (1 point)")
    score += 1
print("")

# Check 8: action_holiday_hours in actions
print("Check 8: Verifying action_holiday_hours in actions...")
if not re.search(r"^\s*-\s*action_holiday_hours", content, re.MULTILINE):
    print("❌ Check 8: FAILED - action_holiday_hours missing from actions: (0 points)")
    print("Hint: Add '- action_holiday_hours' under the actions: section.")
else:
    print(" Check 8: PASSED - action_holiday_hours present (1 point)")
    score += 1
print("")

print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 2.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (file) | Check 2 (slots:) | Check 3 (account + type) | "
    "Check 4 (utter_ask_account) | Check 5 (utter_invalid_account) | "
    "Check 6 (action_check_balance_simple) | Check 7 (action_bank_hours) | Check 8 (action_holiday_hours)"
)
print(f"Score: {score}/{max_score}")

sys.exit(0 if score >= max_score else 1)