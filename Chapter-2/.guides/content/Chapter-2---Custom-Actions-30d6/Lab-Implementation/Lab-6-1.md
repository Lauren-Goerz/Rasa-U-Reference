# Lab 6.1: Training and Testing with Actions - Assessment Setup

## Overview

The **Lab 6.1** guide page covers Level 1 vs Level 2 training, prerequisites, **`cd level2`** + **`rasa train`**, what training does, then the Check It!.

This assessment verifies that students can successfully train their agent with actions and that the training completes without errors.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:

.guides/secure/level2_graders/lab_6.1_grader.sh

## Grader Script

The grader checks only what the lab instructs: model file exists under `models/` and training completed without errors (per verification). No check for virtual environment, model recency, or action files.

```bash
#!/bin/bash
cd /home/codio/workspace/level2

score=0
max_score=4

echo "Running Lab 6.1 Assessment Checks..."
echo ""

# Check 1: Model file exists (2 points) - "A model file (.tar.gz) will be created in the models/ folder" / verification: "A model file exists under models/"
echo "Check 1: Verifying model file exists..."
if [ -d "models" ] && [ -n "$(ls -A models/*.tar.gz 2>/dev/null)" ]; then
    echo " Check 1: PASSED - Model file created (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 1: FAILED - No model file found in models/ directory (0 points)"
    echo "Hint: Run 'python -m rasa train' (with venv activated) to create the model"
fi
echo ""

# Check 2: Training completed without errors (2 points) - verification: "Training completed without errors"
echo "Check 2: Checking for errors in logs..."
if [ -f "logs/logs.out" ]; then
    if grep -qi "error\|exception\|failed" logs/logs.out 2>/dev/null; then
        echo "⚠️  WARNING: Possible errors found in logs. Review logs/logs.out"
        echo "❌ Check 2: FAILED - Logs suggest training may have had errors (0 points)"
    else
        echo " Check 2: PASSED - No obvious errors in logs (2 points)"
        score=$((score + 2))
    fi
else
    echo " Check 2: PASSED - No log file found (training may not have logged) (2 points)"
    score=$((score + 2))
fi
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo " PASS: Training verification complete! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
fi
echo "=========================================="
echo ""
echo "Summary: Check 1 (model exists) | Check 2 (no errors)"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi
```

### Example student deliverable (for grading reference)

Students do not produce a new script file; they run training so that a model is produced. The grader checks that a model file exists in `models/` and that training completed without errors. Example commands (venv activated from project root):

```bash
cd level2
python -m rasa train
```

A successful run produces a `.tar.gz` model under `models/`; the grader expects at least one model file and no errors in logs.

## Assessment Setup and Configuration

1. **Navigate** to the Lab 6.1 section in the Codio Guide Editor.

2. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure each tab as follows.

   **General** – Name: *Lab 6.1: Training and Testing with Actions*. Description: *Verify that students can successfully train their agent with actions*. Points: `4`. Language: `Bash`.

   **Execution** – COMMAND: `bash /home/codio/workspace/.guides/secure/level2_graders/lab_6.1_grader.sh`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace/level2`.

   **Grading**
   - **Points**: `4` – Total points for this assessment.
   - **Allow partial points**: `OFF` – Single run; the script reports one pass/fail outcome, so partial credit is not used.
   - **Use maximum score**: `OFF` – No cap; the student can earn the full point value.
   - **Case insensitive**: `ON` – Output comparison ignores letter case so minor casing differences do not fail the test.
   - **Ignore white spaces**: `ON` – Extra spaces or newlines in the script output do not cause a failure.
   - **Substring match**: `ON` – Pass if the expected string appears anywhere in the output (full output need not match exactly).
   - **Test case** (one case):
     - **INPUT – Arguments**: leave empty – No command-line arguments are passed to the script.
     - **INPUT – STDIN**: leave empty – No stdin is fed to the script.
     - **Expected output**: ` PASS: Training verification complete!` (include the leading space) – The test passes when the script’s stdout contains this string (i.e. when all checks pass).
   - **Show expected answer**: `ALWAYS` – Students can see the required output phrase after submission.
   - **Show rationale to student**: `NEVER` (or as desired) – Controls whether the instructor rationale is shown to the student.
   - **Defined number of attempts**: `OFF` – No limit on submission attempts (or set a limit if desired).
   - **Rationale** (optional): e.g. *The grader checks that a model file exists under models/ and that training completed without errors (per lab verification).*

   **Files** – Create the grader script at `.guides/secure/level2_graders/lab_6.1_grader.sh`. In the Codio workspace terminal (from the workspace root), make it executable: `chmod +x .guides/secure/level2_graders/lab_6.1_grader.sh`.

3. **Save & Test** the assessment. Enable **Learning Analytics** if desired.

---
