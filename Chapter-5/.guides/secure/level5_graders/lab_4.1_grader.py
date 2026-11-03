#!/usr/bin/env python3
"""
Lab 5.4.1: Training the chapter 5 Agent - Grader Script
WARNING is used for partial / stale model / log issues.

Runs from workspace root, verifies venv, then checks chapter5 for:
  - model file
  - recent model
  - clean logs
  - EnterpriseSearchPolicy in config.yml policies
  - pattern_search overridden to call action_trigger_search
No third-party dependencies. Runs from any Python 3 interpreter.
"""

import os
import re
import sys
import time
from pathlib import Path

WORKSPACE_ROOT = Path("/home/codio/workspace")
chapter5_DIR = WORKSPACE_ROOT / "chapter5"
VENV_DIR = WORKSPACE_ROOT / ".venv"
MODELS_DIR = chapter5_DIR / "models"
LOGS_FILE = chapter5_DIR / "logs" / "logs.out"
CONFIG_PATH = chapter5_DIR / "config.yml"
DATA_DIR = chapter5_DIR / "data"

score = 0
max_score = 12

print("Running Lab 5.4.1 Assessment Checks...")
print("")

# ── Check 1: Virtual environment (2 points) ──────────────────────────────────
print("Check 1: Verifying virtual environment...")
if not VENV_DIR.exists():
    print("Check 1: FAILED")
    print("Hint: From the project root, run 'python3 -m venv venv' then activate it.")
    print("FAIL")
    sys.exit(1)

venv_python = VENV_DIR / "bin" / "python"
if not venv_python.exists():
    venv_python = VENV_DIR / "Scripts" / "python.exe"
if not venv_python.exists():
    print("Check 1: FAILED")
    print("Hint: Virtual environment Python not found.")
    print("FAIL")
    sys.exit(1)

print("Check 1: PASSED")
print("Virtual environment found (2 points)")
score += 2
print("")

if not chapter5_DIR.exists():
    print("ERROR: chapter5 directory not found in workspace root")
    print("FAIL")
    sys.exit(1)
os.chdir(chapter5_DIR)

# ── Check 2: Model file exists (2 points) ────────────────────────────────────
print("Check 2: Verifying model file exists...")
if not MODELS_DIR.exists():
    print("Check 2: FAILED")
    print("Hint: Run 'cd chapter5' then 'python -m rasa train' (with venv activated).")
    print("FAIL")
    sys.exit(1)

model_files = list(MODELS_DIR.glob("*.tar.gz"))
if not model_files:
    print("Check 2: FAILED")
    print("Hint: Run 'cd chapter5' then 'python -m rasa train' (with venv activated).")
    print("FAIL")
    sys.exit(1)

print("Check 2: PASSED")
print("Model file found (2 points)")
score += 2
print("")

# ── Check 3: Model is recent (2 points) ──────────────────────────────────────
print("Check 3: Verifying model was trained recently...")
newest_model = max(model_files, key=lambda p: p.stat().st_mtime)
model_age_seconds = time.time() - newest_model.stat().st_mtime
model_age_minutes = model_age_seconds / 60

if model_age_minutes < 10:
    print("Check 3: PASSED")
    print("Model file is recent (2 points)")
    score += 2
else:
    print(f"WARNING: Model file is {model_age_minutes:.1f} minutes old.")
    print("Check 3: PARTIAL")
    print("Model exists but older than 10 minutes (0 points)")
    print("Hint: Re-run 'python -m rasa train' from chapter5 to get a fresh model.")
print("")

# ── Check 4: Logs (2 points) ─────────────────────────────────────────────────
print("Check 4: Checking for errors in logs...")
if LOGS_FILE.exists():
    try:
        with open(LOGS_FILE, "r", encoding="utf-8", errors="ignore") as f:
            log_content = f.read().lower()
        error_keywords = ["error", "exception", "failed"]
        has_errors = any(kw in log_content for kw in error_keywords)
        if has_errors:
            print("WARNING: Possible errors found in chapter5/logs/logs.out.")
            print("Check 4: PARTIAL")
            print("Logs may contain errors (0 points)")
            print("Hint: Open chapter5/logs/logs.out and resolve any errors before re-training.")
        else:
            print("Check 4: PASSED")
            print("No obvious errors in logs (2 points)")
            score += 2
    except Exception as e:
        print(f"WARNING: Could not read log file: {e}")
        print("Check 4: PARTIAL")
        print("Could not verify logs (0 points)")
else:
    print("Check 4: PASSED")
    print("No log file found (2 points)")
    score += 2
print("")

# ── Check 5: EnterpriseSearchPolicy in config.yml policies (2 points) ────────
print("Check 5: Verifying chapter5/config.yml uses EnterpriseSearchPolicy...")
if not CONFIG_PATH.exists():
    print("Check 5: FAILED")
    print("Hint: Ensure you are working in the course chapter5 folder with config.yml present.")
else:
    config = CONFIG_PATH.read_text(encoding="utf-8")
    if re.search(r"EnterpriseSearchPolicy", config):
        print("Check 5: PASSED")
        print("EnterpriseSearchPolicy found in policies (2 points)")
        score += 2
    else:
        print("Check 5: FAILED")
        print(
            "Hint: Add EnterpriseSearchPolicy to the policies section of chapter5/config.yml, "
            "then re-run 'python -m rasa train'."
        )
print("")

# ── Check 6: pattern_search overrides calls action_trigger_search (2 points) ─
print("Check 6: Verifying pattern_search is overridden to call action_trigger_search...")

def _find_pattern_search_override(data_dir: Path) -> tuple[bool, bool]:
    """
    Returns (found_override, calls_action_trigger_search).
    Walks all .yml files under data_dir looking for a flow with id: pattern_search
    that contains a step calling action_trigger_search.
    """
    if not data_dir.exists():
        return False, False

    for yml_file in data_dir.rglob("*.yml"):
        try:
            content = yml_file.read_text(encoding="utf-8")
            if "pattern_search" not in content:
                continue
            if not re.search(r"^\s{2}pattern_search\s*:", content, re.MULTILINE):
                continue
            if "action_trigger_search" in content:
                return True, True
            return True, False
        except Exception:
            continue
    return False, False


found_override, calls_trigger = _find_pattern_search_override(DATA_DIR)

if not found_override:
    print("Check 6: FAILED")
    print(
        "Hint: Add a flow with id 'pattern_search' to a file in chapter5/data/ that calls "
        "action_trigger_search. Without this override, knowledge questions will not reach "
        "EnterpriseSearchPolicy."
    )
elif not calls_trigger:
    print("Check 6: FAILED")
    print("Hint: Make sure your pattern_search override includes a step that calls action_trigger_search.")
else:
    print("Check 6: PASSED")
    print("pattern_search override calls action_trigger_search (2 points)")
    score += 2
print("")

# ── Summary ───────────────────────────────────────────────────────────────────
print("==========================================")
if score >= max_score:
    print(f"PASS: Lab 5.4.1 verification complete! Score: {score}/{max_score}")
else:
    print(f"FAIL: Score {score}/{max_score} - Review the failed checks above and try again.")
print("==========================================")
print("")
print(
    "Summary: Check 1 (venv) | Check 2 (model file) | Check 3 (recent model) | "
    "Check 4 (logs) | Check 5 (EnterpriseSearchPolicy) | Check 6 (pattern_search override)"
)
print(f"Score: {score}/{max_score}")

if score >= max_score:
    sys.exit(0)
sys.exit(1)