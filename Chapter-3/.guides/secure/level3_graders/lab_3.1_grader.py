#!/usr/bin/env python3
"""
Lab 4.1: Writing the Action That Uses the Slot - Grader Script
Output format matches Chapter 2 Lab 6.2 / Chapter 3 Lab 3.1: Check 1–7 (1-based),
leading space on PASSED lines, ========== summary band.

Checks chapter3/actions/action_check_balance_simple.py.
Runs from workspace root; expects /home/codio/workspace.
"""

import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
ACTION_PATH = WORKSPACE_ROOT / "chapter3" / "actions" / "action_check_balance_simple.py"

score = 0
max_score = 8

print("Running Lab 4.1 Assessment Checks...")
print("")

# Check 1: Action file exists
print("Check 1: Verifying action file exists...")
if not ACTION_PATH.exists():
    print("❌ Check 1: FAILED - chapter3/actions/action_check_balance_simple.py not found (0 points)")
    print("Hint: Create the file in chapter3/actions/ with the name action_check_balance_simple.py")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - action file exists (1 point)")
score += 1
print("")

try:
    content = ACTION_PATH.read_text(encoding="utf-8")
except Exception as e:
    print("❌ Check 2: FAILED - Could not read the action file (0 points)")
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
    print(" Check 2: PASSED - Action, Tracker, and CollectingDispatcher (or dispatcher) present (2 points)")
    score += 2
else:
    print("❌ Check 2: FAILED - Missing or incorrect imports (0 points)")
    print("Hint: Import Action, Tracker from rasa_sdk and CollectingDispatcher from rasa_sdk.executor")
print("")

# Check 3: Class ActionCheckBalanceSimple(Action) (1 point)
print("Check 3: Verifying class definition...")
if re.search(r"class\s+ActionCheckBalanceSimple\s*\(\s*Action\s*\)", content):
    print(" Check 3: PASSED - ActionCheckBalanceSimple(Action) found (1 point)")
    score += 1
else:
    print("❌ Check 3: FAILED - Class ActionCheckBalanceSimple(Action) not found (0 points)")
    print("Hint: Define class ActionCheckBalanceSimple(Action):")
print("")

# Check 4: name() returns "action_check_balance_simple" (1 point)
print("Check 4: Verifying name() method...")
if re.search(r'return\s+["\']action_check_balance_simple["\']', content) or (
    "action_check_balance_simple" in content and "def name" in content_lower
):
    print(" Check 4: PASSED - name() returns 'action_check_balance_simple' (1 point)")
    score += 1
else:
    print("❌ Check 4: FAILED - name() must return the string 'action_check_balance_simple' (0 points)")
print("")

# Check 5: run() reads account slot (2 points)
print("Check 5: Verifying slot read...")
slot_read = "get_slot" in content and (
    '"account"' in content or "'account'" in content
)
if slot_read:
    print(" Check 5: PASSED - run() reads account slot (tracker.get_slot('account')) (2 points)")
    score += 2
else:
    print("❌ Check 5: FAILED - run() must read the slot with tracker.get_slot('account') (0 points)")
    print("Hint: account = tracker.get_slot('account')")
print("")

# Check 6: Placeholder check and re-prompt (2 points)
#print("Check 6: Verifying placeholder handling and re-prompt...")
#has_utter_ask = "utter_ask_account" in content and "utter_message" in content_lower
#has_placeholder_idea = any(
#    x in content_lower for x in ["placeholder", "account number", "<missing>", "missing"]
#)
#if has_utter_ask and has_placeholder_idea:
#    print(" Check 6: PASSED - Re-prompts with utter_ask_account when slot is placeholder (2 points)")
#    score += 2
#else:
#    if not has_utter_ask:
#        print("❌ Check 6: FAILED - Must call dispatcher.utter_message(response='utter_ask_account') when slot is a placeholder (0 points)")
#    else:
#        print("❌ Check 6: FAILED - Must detect placeholder values and re-prompt (0 points)")
#    print("Hint: If account (lowercased) is in your placeholder list, call dispatcher.utter_message(response='utter_ask_account') and return []")
#print("")

# Check 6: Balance message (1 point)
print("Check 6: Verifying balance message...")
if (
    "utter_message" in content_lower
    and ("balance" in content_lower or "account" in content)
    and "text" in content_lower
):
    print(" Check 6: PASSED - Sends a message with balance/account (1 point)")
    score += 1
else:
    print("❌ Check 6: FAILED - When slot is valid, send a balance/account message via utter_message (0 points)")
print("")

print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 4.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (file) | Check 2 (imports) | Check 3 (class) | Check 4 (name) | "
    "Check 5 (get_slot account) | Check 6 (balance message)"
)
print(f"Score: {score}/{max_score}")

sys.exit(0 if score >= max_score else 1)
