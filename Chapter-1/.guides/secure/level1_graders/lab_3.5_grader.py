#!/usr/bin/env python3
"""
Lab 3.5: Complete Your Agent for Training — grader (Chapter 1 Unit 3).
Runs from workspace root. Checks: domain has utter_hours and utter_balance;
hours.yml and balance.yml exist with correct flow structure.
"""

import os
import sys
from pathlib import Path

WORKSPACE_ROOT = Path(os.environ.get("CODIO_WORKSPACE", os.getcwd()))
if not WORKSPACE_ROOT.is_absolute():
    WORKSPACE_ROOT = Path.cwd()
CHAPTER1_DIR = WORKSPACE_ROOT / "chapter1"
DOMAIN_FILE = CHAPTER1_DIR / "domain" / "basics.yml"
DATA_BASICS = CHAPTER1_DIR / "data" / "basics"
HOURS_FILE = DATA_BASICS / "hours.yml"
BALANCE_FILE = DATA_BASICS / "balance.yml"

score = 0
max_score = 3

print("Running Lab 3.5 Assessment Checks...")
print("")

# Step 1: Domain has utter_hours and utter_balance with Lab 3.5 handout content (1 point)
# Require key phrases so Lab 3.5 cannot be passed with only Lab 3.4's configuration.
print("Step 1: Checking domain for utter_hours and utter_balance (Lab 3.5 content)...")
if not DOMAIN_FILE.is_file():
    print("❌ Step 1: FAILED - domain/basics.yml not found (0 points)")
    print("FAIL")
    sys.exit(1)
text = DOMAIN_FILE.read_text(encoding="utf-8")
if "utter_hours" not in text or "utter_balance" not in text:
    print("❌ Step 1: FAILED - domain must define utter_hours and utter_balance under responses: (0 points)")
    print("Hint: Add both response blocks in Lab 3.5 Step 1.")
    print("FAIL")
    sys.exit(1)
# Require handout phrases so 3.4-only (student-written) content does not pass.
if "Monday" not in text and "9am" not in text:
    print("❌ Step 1: FAILED - utter_hours must use the Lab 3.5 handout text (e.g. Monday, 9am). (0 points)")
    print("Hint: Paste the exact utter_hours block from Lab 3.5 Step 1.")
    print("FAIL")
    sys.exit(1)
if "account number" not in text:
    print("❌ Step 1: FAILED - utter_balance must use the Lab 3.5 handout text (include 'account number'). (0 points)")
    print("Hint: Paste the exact utter_balance block from Lab 3.5 Step 1.")
    print("FAIL")
    sys.exit(1)
print("✅ Step 1: PASSED - Domain has utter_hours and utter_balance (1 point)")
score += 1
print("")

# Step 2: hours.yml exists with flow hours and action utter_hours (1 point)
print("Step 2: Checking data/basics/hours.yml...")
if not HOURS_FILE.is_file():
    print("❌ Step 2: FAILED - data/basics/hours.yml not found (0 points)")
    print("Hint: Create hours.yml with content from Lab 3.5 Step 2.")
    print("FAIL")
    sys.exit(1)
hours_text = HOURS_FILE.read_text(encoding="utf-8")
if "hours" not in hours_text or "utter_hours" not in hours_text or "flows:" not in hours_text:
    print("❌ Step 2: FAILED - hours.yml must contain flow 'hours' with step utter_hours (0 points)")
    print("FAIL")
    sys.exit(1)
print("✅ Step 2: PASSED - hours.yml has correct structure (1 point)")
score += 1
print("")

# Step 3: balance.yml exists with flow balance and action utter_balance (1 point)
print("Step 3: Checking data/basics/balance.yml...")
if not BALANCE_FILE.is_file():
    print("❌ Step 3: FAILED - data/basics/balance.yml not found (0 points)")
    print("Hint: Create balance.yml with content from Lab 3.5 Step 3.")
    print("FAIL")
    sys.exit(1)
balance_text = BALANCE_FILE.read_text(encoding="utf-8")
if "balance" not in balance_text or "utter_balance" not in balance_text or "flows:" not in balance_text:
    print("❌ Step 3: FAILED - balance.yml must contain flow 'balance' with step utter_balance (0 points)")
    print("FAIL")
    sys.exit(1)
print("✅ Step 3: PASSED - balance.yml has correct structure (1 point)")
score += 1
print("")

print("==========================================")
if score >= max_score:
    print(f"✅ PASS: Lab 3.5 complete! Score: {score}/{max_score}")
    print("Your agent is ready for training (Lab 6.1).")
    print("==========================================")
    print("PASS")
    sys.exit(0)
else:
    print(f"❌ FAIL: Lab 3.5 incomplete. Score: {score}/{max_score}")
    print("==========================================")
    print("FAIL")
    sys.exit(1)
