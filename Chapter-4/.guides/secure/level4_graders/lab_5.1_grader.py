#!/usr/bin/env python3
"""
Lab 5.1: Training the Chapter 4 Agent - Grader Script
Output format matches Chapter 2 Lab 6.2 template (⚠️ for partial / stale model / log issues).

Checks chapter4 for venv, model, and logs using plain string matching.
No third-party dependencies. Runs from any Python 3 interpreter.
"""

import os
import sys
import time
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
CHAPTER4_DIR = WORKSPACE_ROOT / "chapter4"
MODELS_DIR = CHAPTER4_DIR / "models"
LOGS_FILE = CHAPTER4_DIR / "logs" / "logs.out"

# Accept any common venv naming convention
VENV_DIR = next(
    (WORKSPACE_ROOT / name for name in [".venv", "venv", "env", ".env"]
     if (WORKSPACE_ROOT / name).exists()),
    WORKSPACE_ROOT / ".venv"  # fallback for error messaging
)

score = 0
max_score = 10

print("Running Lab 5.1 Assessment Checks...")
print("")

# Check 1: Virtual environment exists (2 points)
print("Check 1: Verifying virtual environment...")
if not VENV_DIR.exists():
    print("❌ Check 1: FAILED - Virtual environment not found in project root (0 points)")
    print("Hint: From the project root, run 'python3 -m venv .venv' then activate it")
    print("FAIL")
    sys.exit(1)

venv_python = VENV_DIR / "bin" / "python"
if not venv_python.exists():
    venv_python = VENV_DIR / "Scripts" / "python.exe"
if not venv_python.exists():
    print("❌ Check 1: FAILED - Virtual environment Python not found (0 points)")
    print("FAIL")
    sys.exit(1)

print(f" Check 1: PASSED - Virtual environment found at '{VENV_DIR.name}' (2 points)")
score += 2
print("")

if not CHAPTER4_DIR.exists():
    print("❌ ERROR: chapter4 directory not found in workspace root")
    print("FAIL")
    sys.exit(1)
os.chdir(CHAPTER4_DIR)

# Check 2: Model file exists (2 points)
print("Check 2: Verifying model file exists...")
if not MODELS_DIR.exists():
    print("❌ Check 2: FAILED - chapter4/models/ directory not found (0 points)")
    print("Hint: Run 'cd chapter4' then 'python -m rasa train' (with venv activated)")
    print("FAIL")
    sys.exit(1)
model_files = list(MODELS_DIR.glob("*.tar.gz"))
if not model_files:
    print("❌ Check 2: FAILED - No model file (.tar.gz) in chapter4/models/ (0 points)")
    print("Hint: Run 'cd chapter4' then 'python -m rasa train' (with venv activated)")
    print("FAIL")
    sys.exit(1)
print(" Check 2: PASSED - Model file created (2 points)")
score += 2
print("")

# Check 3: Model is recent (3 points)
print("Check 3: Verifying model is recent...")
newest_model = max(model_files, key=lambda p: p.stat().st_mtime)
model_age_seconds = time.time() - newest_model.stat().st_mtime
model_age_minutes = model_age_seconds / 60
if model_age_minutes < 10:
    print(" Check 3: PASSED - Model file is recent (3 points)")
    score += 3
else:
    print(f"⚠️  WARNING: Model file is old ({model_age_minutes:.1f} minutes). Re-run training to ensure it's current.")
    print("⚠️  Check 3: PARTIAL - Model exists but older than 10 minutes (0 points)")
print("")

# Check 4: Logs (3 points)
print("Check 4: Checking for errors in logs...")
if LOGS_FILE.exists():
    try:
        with open(LOGS_FILE, "r", encoding="utf-8", errors="ignore") as f:
            log_content = f.read().lower()
        error_keywords = ["error", "exception", "failed"]
        has_errors = any(kw in log_content for kw in error_keywords)
        if has_errors:
            print("⚠️  WARNING: Possible errors found in logs. Review chapter4/logs/logs.out")
            print("⚠️  Check 4: PARTIAL - Logs may contain errors (0 points)")
        else:
            print(" Check 4: PASSED - No obvious errors in logs (3 points)")
            score += 3
    except Exception as e:
        print(f"⚠️  WARNING: Could not read log file: {e}")
        print("⚠️  Check 4: PARTIAL - Could not verify logs (0 points)")
else:
    print(" Check 4: PASSED - No log file found (3 points)")
    score += 3
print("")

# Summary
print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 5.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (venv) | Check 2 (model file) | Check 3 (recent model) | Check 4 (logs)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)