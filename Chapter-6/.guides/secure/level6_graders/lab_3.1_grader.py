#!/usr/bin/env python3
"""
Lab 6.3.1: Sub-Agent Config — Grader (chapter 6)

Checks chapter6/sub_agents/branch_appointment_booking/config.yml exists and contains:
- agent name branch_appointment_booking
- protocol RASA
- model_group openai-gpt-5-mini
- connections.mcp_servers name appointment_mcp
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
CONFIG = WORKSPACE_ROOT / "chapter6" / "sub_agents" / "branch_appointment_booking" / "config.yml"

score = 0
max_score = 10

print("Running Lab 6.3.1 Assessment Checks...")
print("")

# Check 1: config exists and is readable (2 points)
print("Check 1: Verifying branch_appointment_booking config.yml exists...")
if not CONFIG.exists():
    print("❌ Check 1: FAILED - chapter6/sub_agents/branch_appointment_booking/config.yml not found (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 1: PASSED - config.yml found (2 points)")
score += 2
print("")

try:
    content = CONFIG.read_text(encoding="utf-8")
except Exception as e:
    print(f"❌ Could not read config: {e}")
    print("FAIL")
    sys.exit(1)

# Check 2: agent name (2 points)
print("Check 2: Verifying agent name is branch_appointment_booking...")
if "name: branch_appointment_booking" not in content:
    print("❌ Check 2: FAILED - config.yml should contain 'name: branch_appointment_booking' (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 2: PASSED - branch_appointment_booking name present (2 points)")
score += 2
print("")

# Check 3: protocol (2 points)
print("Check 3: Verifying protocol RASA...")
if "protocol" not in content or "RASA" not in content:
    print("❌ Check 3: FAILED - config.yml should contain 'protocol: RASA' (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 3: PASSED - protocol present (2 points)")
score += 2
print("")

# Check 4: model_group openai-gpt-5-mini (2 points)
print("Check 4: Verifying configuration.llm model group...")
if "openai-gpt-5-mini" not in content:
    print("❌ Check 4: FAILED - config.yml should set model_group to openai-gpt-5-mini (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 4: PASSED - openai-gpt-5-mini present (2 points)")
score += 2
print("")

# Check 5: mcp_servers name appointment_mcp (2 points)
print("Check 5: Verifying connections.mcp_servers name is appointment_mcp...")
if "mcp_servers" not in content or "name: appointment_mcp" not in content:
    print("❌ Check 5: FAILED - config.yml should contain mcp_servers with name: appointment_mcp (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 5: PASSED - appointment_mcp present (2 points)")
score += 2
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f"✓ PASS: Lab 6.3.1 complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} — review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (config file) | Check 2 (branch_appointment_booking) | Check 3 (protocol) | "
    "Check 4 (openai-gpt-5-mini) | Check 5 (appointment_mcp)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)