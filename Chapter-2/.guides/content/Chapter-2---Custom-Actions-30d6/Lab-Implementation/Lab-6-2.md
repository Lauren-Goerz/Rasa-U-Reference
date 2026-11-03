# Lab 6.2: Training and Testing – Assessment Setup

## Overview

Lab 6.2 is hands-on **Rasa Inspector** testing from **`level2/`**: students create a **`logs`** folder with `mkdir -p logs` or `mkdir logs` on Windows PowerShell, then run `python -m rasa inspect --debug --log-file logs/logs.out`. Domain and training are assessed elsewhere (**Lab 4.1**, **Lab 6.1**).

**Graded assessment** verifies only that the student ran Inspector with the lab’s log path: **`level2/logs/logs.out`** exists and contains evidence that Inspector / the server started (same idea as Level 1 Lab 6.2’s log check).

### Assessment Type

**Code Output Compare** – Runs `lab_6.2_grader.sh`, which:
1. Verifies `level2/logs/logs.out` exists.
2. Verifies the log contains evidence of an Inspector run (e.g. server start, listen, or inspect).

**Task ID (Codio)**: `code-output-compare-1597644299`  
**Assessment JSON**: `.guides/assessments/code-output-compare-1597644299.json`  
**Grader script**: `.guides/secure/level2_graders/lab_6.2_grader.sh`  
**Points**: 11

### Codio Setup

1. Create a **Code Test** (code-output-compare) for Lab 6.2.
2. **Execution** – Command (run from workspace):
   ```bash
   bash /home/codio/workspace/.guides/secure/level2_graders/lab_6.2_grader.sh
   ```
   Do **not** upload or paste the script into the assessment; run it from the workspace so `git pull` keeps the grader in sync.
3. Configure expected output / sequence per `.guides/assessments/code-output-compare-1597644299.json` (substrings `Check 1: PASSED`, `Check 2: PASSED`, `Successfully passed!`).
4. **Points**: 11. Enable **Learning Analytics** if desired.

### Check It! Tag (Level 2 guide)

The Lab 6.2 page in the Level 2 Codio guide (Unit 6, right after Lab 6.1) includes:
`{Check It!|assessment}(code-output-compare-1597644299)`  
so students can run the assessment from the guide.

---

