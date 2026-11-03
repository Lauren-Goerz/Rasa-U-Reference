#!/usr/bin/env python3
"""
Lab 6.2.2: MCP Registration — Grader (chapter 6)

Checks chapter6/endpoints.yml contains a valid mcp_servers entry
with name appointment_mcp, the correct Streamable HTTP URL, and type: http.
"""

import sys
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
if not WORKSPACE_ROOT.exists():
    WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
ENDPOINTS = WORKSPACE_ROOT / "chapter6" / "endpoints.yml"

score = 0
max_score = 10

print("Running Lab 6.2.2 Assessment Checks...")
print("")

# Check 1: endpoints.yml exists and is readable (2 points)
print("Check 1: Verifying chapter6/endpoints.yml exists...")
if not ENDPOINTS.exists():
    print("❌ Check 1: FAILED - chapter6/endpoints.yml not found (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 1: PASSED - endpoints.yml found (2 points)")
score += 2
print("")

try:
    content = ENDPOINTS.read_text(encoding="utf-8")
except Exception as e:
    print(f"❌ Could not read endpoints.yml: {e}")
    print("FAIL")
    sys.exit(1)

# Check 2: mcp_servers block present (2 points)
print("Check 2: Verifying mcp_servers block is present...")
if "mcp_servers" not in content:
    print("❌ Check 2: FAILED - endpoints.yml should contain an mcp_servers block (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 2: PASSED - mcp_servers present (2 points)")
score += 2
print("")

# Check 3: appointment_mcp name (2 points)
print("Check 3: Verifying mcp_servers name is appointment_mcp...")
if "name: appointment_mcp" not in content:
    print("❌ Check 3: FAILED - mcp_servers entry should have 'name: appointment_mcp' (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 3: PASSED - appointment_mcp present (2 points)")
score += 2
print("")

# Check 4: URL contains correct path (2 points)
print("Check 4: Verifying MCP server URL contains 127.0.0.1:8080/mcp...")
if "127.0.0.1:8080/mcp" not in content:
    print("❌ Check 4: FAILED - URL should be http://127.0.0.1:8080/mcp (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 4: PASSED - URL is correct (2 points)")
score += 2
print("")

# Check 5: type: http (2 points)
print("Check 5: Verifying type: http is set...")
if "type: http" not in content:
    print("❌ Check 5: FAILED - mcp_servers entry should include 'type: http' (0 points)")
    print("FAIL")
    sys.exit(1)
print("✓ Check 5: PASSED - type: http present (2 points)")
score += 2
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f"✓ PASS: Lab 6.2.2 complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} — review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (endpoints.yml) | Check 2 (mcp_servers) | Check 3 (appointment_mcp) | "
    "Check 4 (URL) | Check 5 (type: http)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)