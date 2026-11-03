#!/usr/bin/env python3
"""
Lab 6.4.1: Adding a Flow to Call a Sub-Agent

Checks chapter6/data/basics/book_appointment.yml exists and contains:
- flow id book_appointment
- call: branch_appointment_booking step
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
FLOW = WORKSPACE_ROOT / "chapter6" / "data" / "basics" / "book_appointment.yml"

score = 0
max_score = 10

print("Running Lab 6.4.1 Assessment Checks...")
print("")

# Check 1: file exists and is readable (3 points)
print("Check 1: Verifying book_appointment.yml exists...")
if not FLOW.exists():
    print("❌ Check 1: FAILED - chapter6/data/basics/book_appointment.yml not found (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 1: PASSED - flow file found (3 points)")
score += 3
print("")

try:
    content = FLOW.read_text(encoding="utf-8")
except Exception as e:
    print(f"❌ Could not read flow file: {e}")
    print("FAIL")
    sys.exit(1)

# Check 2: flow id present (3 points)
print("Check 2: Verifying flow id book_appointment...")
if "book_appointment" not in content:
    print("❌ Check 2: FAILED - flow id book_appointment not found (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 2: PASSED - flow id present (3 points)")
score += 3
print("")

# Check 3: call: branch_appointment_booking step (4 points)
print("Check 3: Verifying call: branch_appointment_booking step...")
if "call: branch_appointment_booking" not in content:
    print("❌ Check 3: FAILED - 'call: branch_appointment_booking' not found — must match agent.name in sub-agent config (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 3: PASSED - call: branch_appointment_booking present (4 points)")
score += 4
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f"✓ PASS: Lab 6.4.1 complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} — review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (flow file) | Check 2 (flow id) | Check 3 (call: branch_appointment_booking)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)