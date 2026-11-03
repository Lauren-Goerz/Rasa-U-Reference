Lab 5.3.1 grader · PY
Copy

#!/usr/bin/env python3
"""
Lab 5.3.1: Override pattern_search - Grader Script
Checks that data/basics/pattern_search.yml exists and is correctly configured.
No third-party dependencies. Runs from any Python 3 interpreter.
"""
 
import re
import sys
from pathlib import Path
 
WORKSPACE_ROOT = Path("/home/codio/workspace")
PATTERN_SEARCH_PATH = WORKSPACE_ROOT / "chapter5" / "data" / "basics" / "pattern_search.yml"
 
score = 0
max_score = 4
 
print("Running Lab 5.3.1 Assessment Checks...")
print("")
 
# Check 1: pattern_search.yml exists (1 point)
print("Check 1: Verifying pattern_search.yml exists...")
if not PATTERN_SEARCH_PATH.exists():
    print("❌ Check 1: FAILED - chapter5/data/basics/pattern_search.yml not found (0 points)")
    print("Hint: Create the file at exactly that path. The folder structure must be data/basics/ inside chapter5/.")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - pattern_search.yml found (1 point)")
score += 1
print("")
 
content = PATTERN_SEARCH_PATH.read_text(encoding="utf-8")
 
# Check 2: flow id is exactly pattern_search (1 point)
print("Check 2: Verifying flow id is exactly 'pattern_search'...")
if re.search(r"^\s{2}pattern_search\s*:", content, re.MULTILINE):
    print(" Check 2: PASSED - flow id pattern_search found (1 point)")
    score += 1
else:
    print("❌ Check 2: FAILED - flow id 'pattern_search' not found (0 points)")
    print("Hint: The flow id must be exactly 'pattern_search' — this is what tells Rasa to override the built-in pattern.")
print("")
 
# Check 3: action_trigger_search is the step (1 point)
print("Check 3: Verifying action_trigger_search is the flow step...")
if re.search(r"action:\s*action_trigger_search", content):
    print(" Check 3: PASSED - action_trigger_search found (1 point)")
    score += 1
else:
    print("❌ Check 3: FAILED - action_trigger_search not found in flow steps (0 points)")
    print("Hint: The flow must have a single step: action: action_trigger_search")
print("")
 
# Check 4: flow has a name and description (1 point)
print("Check 4: Verifying flow has name and description...")
has_name = re.search(r"name:\s*.+", content)
has_description = re.search(r"description:\s*.+", content)
if has_name and has_description:
    print(" Check 4: PASSED - name and description present (1 point)")
    score += 1
else:
    missing = []
    if not has_name:
        missing.append("name")
    if not has_description:
        missing.append("description")
    print(f"❌ Check 4: FAILED - missing: {missing} (0 points)")
    print("Hint: Add a name: and description: field to the flow as shown in the lab instructions.")
print("")
 
# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 5.3.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (file exists) | Check 2 (flow id) | "
    "Check 3 (action_trigger_search) | Check 4 (name and description)"
)
print(f"Score: {score}/{max_score}")
 
if score >= max_score:
    sys.exit(0)
sys.exit(1)