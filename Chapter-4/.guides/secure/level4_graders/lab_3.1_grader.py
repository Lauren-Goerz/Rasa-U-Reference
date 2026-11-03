#!/usr/bin/env python3
"""
Lab 3.1: Writing the Action That Uses Multiple Slots - Grader Script
Output format matches Chapter 2 Lab 6.2 template (leading space on PASSED lines,
no emoji on pass; ❌ on fail; ========== summary band; exit 0 only on full score).

Checks chapter4/actions/action_process_transfer.py using plain string matching.
No third-party dependencies. Runs from any Python 3 interpreter.
"""

import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
ACTION_PATH = WORKSPACE_ROOT / "chapter4" / "actions" / "action_process_transfer.py"

score = 0
max_score = 10

print("Running Lab 3.1 Assessment Checks...")
print("")

# Check 1: Action file exists (1 point)
print("Check 1: Verifying action file exists...")
if not ACTION_PATH.exists():
    print("❌ Check 1: FAILED - chapter4/actions/action_process_transfer.py not found (0 points)")
    print("Hint: Create the file in chapter4/actions/ with the name action_process_transfer.py")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - action file exists (1 point)")
score += 1
print("")

try:
    content = ACTION_PATH.read_text(encoding="utf-8")
except Exception as e:
    print("❌ FAILED - Could not read the action file:")
    print(f"   {e}")
    print("FAIL")
    sys.exit(1)

content_lower = content.lower()

# Check 2: Required imports (2 points)
print("Check 2: Verifying imports...")
has_action = "action" in content_lower and "rasa_sdk" in content
has_tracker = "tracker" in content_lower and "rasa_sdk" in content
has_dispatcher = "collectingdispatcher" in content_lower or "dispatcher" in content_lower
if has_action and has_tracker and has_dispatcher:
    print(" Check 2: PASSED - Action, Tracker, and CollectingDispatcher present (2 points)")
    score += 2
else:
    print("❌ Check 2: FAILED - Missing or incorrect imports (0 points)")
    print("Hint: Import Action, Tracker from rasa_sdk and CollectingDispatcher from rasa_sdk.executor")
print("")

# Check 3: Class ActionProcessTransfer(Action) (1 point)
print("Check 3: Verifying class definition...")
if re.search(r"class\s+ActionProcessTransfer\s*\(\s*Action\s*\)", content):
    print(" Check 3: PASSED - ActionProcessTransfer(Action) found (1 point)")
    score += 1
else:
    print("❌ Check 3: FAILED - Class ActionProcessTransfer(Action) not found (0 points)")
print("")

# Check 4: name() returns "action_process_transfer" (1 point)
print("Check 4: Verifying name() method...")
if re.search(r'return\s+["\']action_process_transfer["\']', content) or (
    "action_process_transfer" in content and "def name" in content_lower
):
    print(" Check 4: PASSED - name() returns 'action_process_transfer' (1 point)")
    score += 1
else:
    print("❌ Check 4: FAILED - name() must return the string 'action_process_transfer' (0 points)")
print("")

# Check 5: run() reads all three slots (3 points)
print("Check 5: Verifying run() reads amount, recipient, account...")
has_amount = "get_slot" in content and ('"amount"' in content or "'amount'" in content)
has_recipient = "recipient" in content and "get_slot" in content
has_account = "account" in content and "get_slot" in content
if has_amount and has_recipient and has_account:
    print(" Check 5: PASSED - run() reads amount, recipient, account (3 points)")
    score += 3
else:
    missing = []
    if not has_amount:
        missing.append("amount")
    if not has_recipient:
        missing.append("recipient")
    if not has_account:
        missing.append("account")
    print(f"❌ Check 5: FAILED - run() must read all three slots; missing or unclear: {missing} (0 points)")
    print("Hint: amount = tracker.get_slot('amount') or ''; same for recipient and account")
print("")

# Check 6: Sends a message (2 points)
print("Check 6: Verifying confirmation message...")
if "utter_message" in content_lower and (
    "transfer" in content_lower or "amount" in content or "recipient" in content
):
    print(" Check 6: PASSED - Sends a message (e.g. transfer confirmation) (2 points)")
    score += 2
else:
    print(
        "❌ Check 6: FAILED - When slots are valid, send a message "
        "(dispatcher.utter_message(text=...)) (0 points)"
    )
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 3.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (action file) | Check 2 (imports) | Check 3 (class) | "
    "Check 4 (name) | Check 5 (run slots) | Check 6 (utter_message)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)