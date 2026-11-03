#!/usr/bin/env python3
"""
Lab 5.2.0: Create docs/ folder and knowledge files - Grader Script
Checks that chapter5/docs/ exists and contains banking_products.txt and banking_policies.txt.
No third-party dependencies. Runs from any Python 3 interpreter.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
DOCS_DIR = WORKSPACE_ROOT / "chapter5" / "docs"
PRODUCTS_FILE = DOCS_DIR / "banking_products.txt"
POLICIES_FILE = DOCS_DIR / "banking_policies.txt"

score = 0
max_score = 3

print("Running Lab 5.2.0 Assessment Checks...")
print("")

# Check 1: docs/ folder exists (1 point)
print("Check 1: Verifying docs/ folder exists...")
if not DOCS_DIR.exists():
    print("Check 1: FAILED")
    print("Hint: Create the docs/ folder inside chapter5/ with 'mkdir chapter5/docs'.")
    print("FAIL")
    sys.exit(1)
print("Check 1: PASSED")
print("docs/ folder found (1 point)")
score += 1
print("")

# Check 2: banking_products.txt exists (1 point)
print("Check 2: Verifying banking_products.txt exists...")
if not PRODUCTS_FILE.exists():
    print("Check 2: FAILED")
    print("Hint: Create banking_products.txt inside chapter5/docs/ and add the content from the lab instructions.")
else:
    print("Check 2: PASSED")
    print("banking_products.txt found (1 point)")
    score += 1
print("")

# Check 3: banking_policies.txt exists (1 point)
print("Check 3: Verifying banking_policies.txt exists...")
if not POLICIES_FILE.exists():
    print("Check 3: FAILED")
    print("Hint: Create banking_policies.txt inside chapter5/docs/ and add the content from the lab instructions.")
else:
    print("Check 3: PASSED")
    print("banking_policies.txt found (1 point)")
    score += 1
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f"PASS: Lab 5.2.0 verification complete! Score: {score}/{max_score}")
else:
    print(f"FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (docs/ folder) | Check 2 (banking_products.txt) | Check 3 (banking_policies.txt)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)