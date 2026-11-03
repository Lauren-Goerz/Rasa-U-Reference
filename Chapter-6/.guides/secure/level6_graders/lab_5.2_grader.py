#!/usr/bin/env python3
"""
Lab 5.2: Completion Check chapter 6 - Grader
Output format matches chapter 2 Lab 6.2 template.

Verifies chapter 6 artifacts: sub_agent config, mcp_servers in endpoints, ask_banking_assistant flow.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
chapter6 = WORKSPACE_ROOT / "chapter6"

score = 0
max_score = 10

print("Running Lab 5.2 Completion Check...")
print("")

# Check 1: config (3 points)
print("Check 1: Verifying sub-agent config...")
config = chapter6 / "sub_agents" / "banking_assistant" / "config.yml"
if not config.exists():
    print("❌ Check 1: FAILED - chapter6/sub_agents/banking_assistant/config.yml must exist (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 1: PASSED - config.yml exists (3 points)")
score += 3
print("")

# Check 2: endpoints + mcp_servers (4 points)
print("Check 2: Verifying endpoints.yml and mcp_servers...")
endpoints = chapter6 / "endpoints.yml"
if not endpoints.exists():
    print("❌ Check 2: FAILED - chapter6/endpoints.yml must exist (0 points)")
    print("FAIL")
    sys.exit(1)
try:
    ep_text = endpoints.read_text(encoding="utf-8")
except Exception as e:
    print(f"❌ Check 2: FAILED - Could not read endpoints: {e} (0 points)")
    print("FAIL")
    sys.exit(1)
if "mcp_servers" not in ep_text:
    print("❌ Check 2: FAILED - endpoints.yml must contain mcp_servers (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 2: PASSED - endpoints with mcp_servers (4 points)")
score += 4
print("")

# Check 3: flow with call (3 points)
print("Check 3: Verifying ask_banking_assistant flow...")
flow_file = chapter6 / "data" / "basics" / "ask_banking_assistant.yml"
if not flow_file.exists():
    print("❌ Check 3: FAILED - chapter6/data/basics/ask_banking_assistant.yml must exist (0 points)")
    print("FAIL")
    sys.exit(1)
try:
    content = flow_file.read_text(encoding="utf-8")
except Exception as e:
    print(f"❌ Check 3: FAILED - Could not read flow: {e} (0 points)")
    print("FAIL")
    sys.exit(1)
if "call:" not in content or "banking_assistant" not in content:
    print("❌ Check 3: FAILED - Flow must contain call: banking_assistant (0 points)")
    print("FAIL")
    sys.exit(1)
print(" Check 3: PASSED - ask_banking_assistant flow with call step (3 points)")
score += 3
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 5.2 completion check passed! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print("Summary: Check 1 (sub-agent config) | Check 2 (endpoints mcp) | Check 3 (flow)")
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)
