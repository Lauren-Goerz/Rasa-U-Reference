#!/usr/bin/env python3
"""
Lab 6.1: Training and Testing with Slots - Grader Script
Output format matches Chapter 2 Lab 6.2 / Chapter 3 Lab 3.1: Check 1–5 (1-based),
leading space on PASSED lines, ========== summary band.

Runs from workspace root; expects /home/codio/workspace.
"""

import os
import sys
import time
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
CHAPTER3_DIR = WORKSPACE_ROOT / "chapter3"
VENV_DIR = WORKSPACE_ROOT / ".venv"
MODELS_DIR = CHAPTER3_DIR / "models"
LOGS_FILE = CHAPTER3_DIR / "logs" / "logs.out"

score = 0
max_score = 12

print("Running Lab 6.1 Assessment Checks...")
print("")

# Check 1: Virtual environment (2 points)
print("Check 1: Verifying virtual environment...")
if not VENV_DIR.exists():
    print("❌ Check 1: FAILED - Virtual environment (.venv) not found in project root (0 points)")
    print("Hint: From the project root, run 'python3.11 -m venv .venv' then activate it.")
    print("FAIL")
    sys.exit(1)

venv_python = VENV_DIR / "bin" / "python"
if not venv_python.exists():
    venv_python = VENV_DIR / "Scripts" / "python.exe"
if not venv_python.exists():
    print("❌ Check 1: FAILED - Virtual environment Python not found (0 points)")
    print("FAIL")
    sys.exit(1)

print(" Check 1: PASSED - Virtual environment found (2 points)")
score += 2
print("")

if not CHAPTER3_DIR.exists():
    print("❌ Check 2: FAILED - chapter3 directory not found (0 points)")
    print("FAIL")
    sys.exit(1)
os.chdir(CHAPTER3_DIR)

model_files = []

# Check 2: Model file exists (2 points)
print("Check 2: Verifying model file exists...")
if not MODELS_DIR.exists():
    print("❌ Check 2: FAILED - models/ directory not found (0 points)")
    print("Hint: Run 'cd chapter3' then 'python -m rasa train' with venv activated.")
    print("FAIL")
    sys.exit(1)
model_files = list(MODELS_DIR.glob("*.tar.gz"))
if model_files:
    print(" Check 2: PASSED - Model file created (2 points)")
    score += 2
else:
    print("❌ Check 2: FAILED - No model file found in models/ (0 points)")
    print("Hint: Run 'cd chapter3' then 'python -m rasa train' with venv activated.")
    print("FAIL")
    sys.exit(1)
print("")

# Check 3: Model is recent (3 points)
print("Check 3: Verifying model is recent...")
newest_model = max(model_files, key=lambda p: p.stat().st_mtime)
model_age_minutes = (time.time() - newest_model.stat().st_mtime) / 60

if model_age_minutes < 10:
    print(" Check 3: PASSED - Model file is recent (training within 10 minutes) (3 points)")
    score += 3
else:
    print(f"⚠️  Check 3: PARTIAL - Model is {model_age_minutes:.1f} minutes old; re-run training for full credit (0 points)")
print("")

# Check 4: Logs (3 points)
print("Check 4: Checking for errors in logs...")
if LOGS_FILE.exists():
    try:
        log_content = LOGS_FILE.read_text(encoding="utf-8", errors="ignore").lower()
        error_keywords = ["error", "exception", "failed"]
        has_errors = any(kw in log_content for kw in error_keywords)
        if has_errors:
            print("⚠️  Check 4: PARTIAL - Logs may contain errors; review logs/logs.out (0 points)")
        else:
            print(" Check 4: PASSED - No obvious errors in logs (3 points)")
            score += 3
    except OSError as e:
        print(f"⚠️  Check 4: PARTIAL - Could not read log file ({e}) (0 points)")
else:
    print(" Check 4: PASSED - No log file (training may not have logged yet) (3 points)")
    score += 3
print("")

# Check 5: Training pipeline complete (2 points) — confirms we reached end of checks with a model
print("Check 5: Verifying training artifacts...")
print(" Check 5: PASSED - chapter3 agent has a trained model to run or inspect (2 points)")
score += 2
print("")

print("==========================================")
if score >= max_score:
    print(f" PASS: Lab 6.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"❌ FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (venv) | Check 2 (model file) | Check 3 (recent model) | "
    "Check 4 (logs) | Check 5 (artifacts)"
)
print(f"Score: {score}/{max_score}")

sys.exit(0 if score >= max_score else 1)
