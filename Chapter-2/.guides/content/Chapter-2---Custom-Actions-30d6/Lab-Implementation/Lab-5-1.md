# Lab 5.1: Using Actions in Flows

## Guide Content (For Students)

**Placement**: This lab follows Unit 5: Using Actions in Flows.

**Where to work:** Students do this lab from the **level2** folder. All file paths are relative to `level2`. In Codio, the terminal opens in the workspace (`~/workspace`); they run `cd level2`. Locally, they open the terminal in the main project folder (contains `level1`, `level2`, `.guides`), then run `cd level2`.

**Full instructions:** See **Level2_Lab5.1_Content.md** (and Codio Lab 5.1 guide) for the complete step-by-step: (1) go to `data/basics/`, (2) create `hours.yml` with the `hours` flow and `action_bank_hours`, (3) create `holiday_hours.yml` with the `holiday_hours` flow and `action_holiday_hours`, (4) verify both files, then run the assessment. In Unit 6, **Lab 6.2** covers Inspector setup and example questions (not on the Lab 5.1 student page).

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students can create flow files that use actions: the example `hours.yml` (action_bank_hours) and their own `holiday_hours.yml` (action_holiday_hours), with correct YAML structure. The lab instructs students to work from the **level2** folder (main project folder, then `cd level2`). The grader runs from `level2` and checks files under that directory.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:

.guides/secure/level2_graders/lab_5.1_grader.sh

## Grader Script

The grader checks only what the lab instructs: hours.yml exists with hours flow and action_bank_hours; holiday_hours.yml exists with flow holiday_hours, name/description (explicit for holiday_hours only), and action_holiday_hours. No check for virtual environment; no name/description required for the hours flow.

```bash
#!/bin/bash
cd /home/codio/workspace/level2

score=0
max_score=12

echo "Running Lab 5.1 Assessment Checks..."
echo ""

# Check 1: hours.yml file exists (2 points) - "Ensure the hours flow exists in data/basics/hours.yml"
echo "Check 1: Verifying hours.yml flow file exists..."
if [ ! -f "data/basics/hours.yml" ]; then
    echo "❌ Check 1: FAILED - data/basics/hours.yml not found (0 points)"
    echo "Hint: Create hours.yml in the data/basics/ folder"
else
    echo " Check 1: PASSED - hours.yml file exists (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 2: hours flow exists (1 point) - explicit
echo "Check 2: Verifying hours flow exists..."
if [ -f "data/basics/hours.yml" ] && grep -q "^flows:" data/basics/hours.yml 2>/dev/null && grep -q "^  hours:" data/basics/hours.yml 2>/dev/null; then
    echo " Check 2: PASSED - hours flow found (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 2: FAILED - hours flow not found (0 points)"
    echo "Hint: Add 'flows:' and '  hours:' to hours.yml"
fi
echo ""

# Check 3: hours flow uses action_bank_hours (2 points) - explicit
echo "Check 3: Verifying flow uses action_bank_hours..."
if [ -f "data/basics/hours.yml" ] && grep -q "action_bank_hours" data/basics/hours.yml 2>/dev/null; then
    if awk '/steps:/,/^[a-z]/ {if (/action_bank_hours/) found=1} END {exit !found}' data/basics/hours.yml 2>/dev/null; then
        echo " Check 3: PASSED - action_bank_hours is used in steps (2 points)"
        score=$((score + 2))
    else
        echo "⚠️  Check 3: PARTIAL - action_bank_hours found but may not be in steps (1 point)"
        score=$((score + 1))
    fi
else
    echo "❌ Check 3: FAILED - action_bank_hours not found in flow (0 points)"
    echo "Hint: Add '- action: action_bank_hours' under steps:"
fi
echo ""

# Check 4: holiday_hours.yml exists (2 points) - "Create data/basics/holiday_hours.yml"
echo "Check 4: Verifying holiday_hours.yml flow file exists..."
if [ ! -f "data/basics/holiday_hours.yml" ]; then
    echo "❌ Check 4: FAILED - data/basics/holiday_hours.yml not found (0 points)"
    echo "Hint: Create holiday_hours.yml in the data/basics/ folder (flow for your action from Lab 3.1)"
else
    echo " Check 4: PASSED - holiday_hours.yml file exists (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 5: holiday_hours flow with flow id, steps, action_holiday_hours (2 points) - explicit
echo "Check 5: Verifying holiday_hours flow structure..."
if [ -f "data/basics/holiday_hours.yml" ] && grep -q "^flows:" data/basics/holiday_hours.yml 2>/dev/null && grep -q "^  holiday_hours:" data/basics/holiday_hours.yml 2>/dev/null && grep -q "action_holiday_hours" data/basics/holiday_hours.yml 2>/dev/null; then
    if grep -q "steps:" data/basics/holiday_hours.yml 2>/dev/null; then
        echo " Check 5: PASSED - holiday_hours flow has flows:, holiday_hours:, and uses action_holiday_hours (2 points)"
        score=$((score + 2))
    else
        echo "⚠️  Check 5: PARTIAL - flow found but steps: may be missing (1 point)"
        score=$((score + 1))
    fi
else
    echo "❌ Check 5: FAILED - holiday_hours.yml needs flows:, a flow named holiday_hours:, and - action: action_holiday_hours (0 points)"
    echo "Hint: Add flows: then '  holiday_hours:' with name:, description:, steps: and - action: action_holiday_hours"
fi
echo ""

# Check 6: holiday_hours flow has name and description (1 point) - explicit in instructions
echo "Check 6: Verifying holiday_hours flow has name and description..."
if [ -f "data/basics/holiday_hours.yml" ] && grep -q "name:" data/basics/holiday_hours.yml 2>/dev/null && grep -q "description:" data/basics/holiday_hours.yml 2>/dev/null; then
    echo " Check 6: PASSED - Flow has name and description (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 6: FAILED - Flow missing name or description (0 points)"
    echo "Hint: Add name: and description: to your holiday_hours flow so the LLM can match user questions"
fi
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo " PASS: Flow creation verification complete! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
fi
echo "=========================================="
echo ""
echo "Summary: Check 1-3 (hours.yml) | Check 4-6 (holiday_hours.yml)"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi
```

### Example student deliverable (for grading reference)

Students create **`data/basics/hours.yml`** and **`data/basics/holiday_hours.yml`** (neither is in the Level 2 starter). Example contents:

**`data/basics/hours.yml`** (example flow; Lab 5.1):

```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours
```

**`data/basics/holiday_hours.yml`** (student-created flow):

```yaml
flows:
  holiday_hours:
    name: holiday hours
    description: Tell the user about holiday schedule and whether we're closed today.
    steps:
      - action: action_holiday_hours
```

## Assessment Setup and Configuration

**Codio: Grader updates from GitHub**  
To have grader changes (pushed to GitHub and pulled on Codio) take effect automatically, the assessment **must run the script from the workspace**, not use an uploaded or pasted copy. In **Execution**, set the COMMAND to run the file path below. Do **not** upload or embed the script content in the assessment; otherwise Codio runs a stored copy and `git pull` will not update the grader.

1. **Navigate** to the Lab 5.1 section in the Codio Guide Editor.

2. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure each tab as follows.

   **General** – Name: *Lab 5.1: Using Actions in Flows*. Description: *Verify that students can create flows that use actions (hours.yml and holiday_hours.yml)*. Points: `12`. Language: `Bash`.

   **Execution** – COMMAND: `bash /home/codio/workspace/.guides/secure/level2_graders/lab_5.1_grader.sh`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace/level2`. (This runs the script from the workspace so `git pull` updates the grader.)

   **Grading**
   - **Points**: `12` – Total points for this assessment.
   - **Allow partial points**: `OFF` – Single run; the script reports one pass/fail outcome, so partial credit is not used.
   - **Use maximum score**: `OFF` – No cap; the student can earn the full point value.
   - **Case insensitive**: `ON` – Output comparison ignores letter case so minor casing differences do not fail the test.
   - **Ignore white spaces**: `ON` – Extra spaces or newlines in the script output do not cause a failure.
   - **Substring match**: `ON` – Pass if the expected string appears anywhere in the output (full output need not match exactly).
   - **Test case** (one case):
     - **INPUT – Arguments**: leave empty – No command-line arguments are passed to the script.
     - **INPUT – STDIN**: leave empty – No stdin is fed to the script.
     - **Expected output**: ` PASS: Flow creation verification complete!` (include the leading space) – The test passes when the script’s stdout contains this string (i.e. when all checks pass).
   - **Show expected answer**: `ALWAYS` – Students can see the required output phrase after submission.
   - **Show rationale to student**: `NEVER` (or as desired) – Controls whether the instructor rationale is shown to the student.
   - **Defined number of attempts**: `OFF` – No limit on submission attempts (or set a limit if desired).
   - **Rationale** (optional): e.g. *The grader checks that `data/basics/hours.yml` and `data/basics/holiday_hours.yml` exist and define flows that use the correct actions.*

   **Files** – Ensure the grader script exists at `.guides/secure/level2_graders/lab_5.1_grader.sh` (it is in the repo). Do **not** upload or paste the script into the assessment; the Execution command above runs this file from the workspace so that `git pull` keeps the grader in sync. From the workspace root: `chmod +x .guides/secure/level2_graders/lab_5.1_grader.sh` if needed.

3. **Save & Test** the assessment. Enable **Learning Analytics** if desired.

---
