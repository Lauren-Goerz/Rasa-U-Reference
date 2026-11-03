#!/usr/bin/env python3
"""
Lab 2.1: Adding Multiple Slots in the Domain - Grader Script
Output format matches Chapter 2 Lab 6.2 template (leading space on PASSED lines,
no emoji on pass; ❌ on fail; ========== summary band; exit 0 only on full score).

Checks chapter4/domain/basics.yml using plain string matching.
No third-party dependencies. Runs from any Python 3 interpreter.
"""

import re
import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
DOMAIN_PATH = WORKSPACE_ROOT / "chapter4" / "domain" / "basics.yml"

score = 0
max_score = 12

print("Running Lab 2.1 Assessment Checks...")
print("")

# Check 1: Domain file exists (1 point)
print("Check 1: Verifying domain file exists...")
if not DOMAIN_PATH.exists():
    print("❌ Check 1: FAILED - chapter4/domain/basics.yml not found (0 points)")
    print("Hint: Add domain/basics.yml in the chapter4 folder with slots, responses, and actions.")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - domain file exists (1 point)")
score += 1
print("")

content = DOMAIN_PATH.read_text(encoding="utf-8")

# Check 2: slots amount, recipient, account (3 points)
print("Check 2: Verifying slots amount, recipient, account...")
has_amount = re.search(r"^\s{2}amount\s*:", content, re.MULTILINE)
has_recipient = re.search(r"^\s{2}recipient\s*:", content, re.MULTILINE)
has_account = re.search(r"^\s{2}account\s*:", content, re.MULTILINE)
missing_slots = []
if not has_amount:
    missing_slots.append("amount")
if not has_recipient:
    missing_slots.append("recipient")
if not has_account:
    missing_slots.append("account")
if not missing_slots:
    print(" Check 2: PASSED - transfer slots and account slot present (3 points)")
    score += 3
else:
    print(f"❌ Check 2: FAILED - missing slots: {missing_slots} (0 points)")
    print("Hint: Add amount, recipient, account under slots: with type: text")
print("")

# Check 3: utter_ask_amount, utter_ask_recipient, utter_ask_account (3 points)
print("Check 3: Verifying ask responses...")
missing_asks = []
for r in ["utter_ask_amount", "utter_ask_recipient", "utter_ask_account"]:
    if not re.search(rf"^\s+{r}\s*:", content, re.MULTILINE):
        missing_asks.append(r)
if not missing_asks:
    print(" Check 3: PASSED - transfer asks and utter_ask_account present (3 points)")
    score += 3
else:
    print(f"❌ Check 3: FAILED - missing or empty ask responses: {missing_asks} (0 points)")
    print("Hint: Add utter_ask_amount, utter_ask_recipient, utter_ask_account under responses:")
print("")

# Check 4: action_process_transfer in actions (2 points)
print("Check 4: Verifying action_process_transfer in actions...")
if re.search(r"^\s*-\s*action_process_transfer", content, re.MULTILINE):
    print(" Check 4: PASSED - action_process_transfer registered (2 points)")
    score += 2
else:
    print("❌ Check 4: FAILED - action_process_transfer not in actions list (0 points)")
    print("Hint: Add - action_process_transfer under the actions: section")
print("")

# Check 5: Chapter 2/3 actions still registered (3 points)
print("Check 5: Verifying Chapter 2/3 actions still in domain...")
missing_legacy = []
for a in ["action_bank_hours", "action_holiday_hours", "action_check_balance_simple"]:
    if not re.search(rf"^\s*-\s*{a}", content, re.MULTILINE):
        missing_legacy.append(a)
if not missing_legacy:
    print(" Check 5: PASSED - action_bank_hours, action_holiday_hours, action_check_balance_simple present (3 points)")
    score += 3
else:
    print(f"❌ Check 5: FAILED - missing actions: {missing_legacy} (0 points)")
    print(
        "Hint: Do not replace the whole actions: list when adding action_process_transfer. "
        "Keep action_bank_hours, action_holiday_hours, and action_check_balance_simple."
    )
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 2.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (domain file) | Check 2 (slots) | "
    "Check 3 (ask responses) | Check 4 (action_process_transfer) | "
    "Check 5 (Chapter 2/3 actions preserved)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)