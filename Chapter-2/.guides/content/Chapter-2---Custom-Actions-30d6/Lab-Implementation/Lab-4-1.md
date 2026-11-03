# Lab 4.1: Registering Actions in the Domain

## Guide Content (For Students)

**Placement**: This lab follows Unit 4: Registering Actions in the Domain.

---

### Your Task

Add an `actions:` section to `domain/basics.yml` and register **both** (the Level 2 starter has responses only—no `actions:` section yet):

- **action_bank_hours** – the example action you studied in the units  
- **action_holiday_hours** – the action you created in Lab 3.1  

Each action must appear as a list item under `actions:` (e.g. `- action_bank_hours`).

---

### Verification

Before submitting, confirm:

- The file `domain/basics.yml` has an `actions:` section  
- Both `action_bank_hours` and `action_holiday_hours` are listed  
- YAML is valid (correct indentation and dashes)  

Run the assessment when you’re done.

{Check It!|assessment}(code-output-compare-1451983168)

---

#### Review in Inspector (optional)

After the assessment, train and open the Rasa Inspector GUI (see Level 1 **Lab 6.2**). In the chat, try **"What are your hours?"** (should work if the `hours` flow exists) and **"What are your holiday hours?"** (likely not yet, you'll add that flow in Unit 5).

---

## Assessment Setup (For Implementers)

## Overview

This assessment verifies that students can register actions in the domain file with correct YAML syntax, including both the example action and the action they created in Lab 3.1.

### Assessment Type

**Standard Code Test** (Bash script)

## Grader Script Location

Save the grader script at:

.guides/secure/level2_graders/lab_4.1_grader.sh

## Grader Script

The grader checks only what the lab instructs: domain file exists, `actions:` section, both `action_bank_hours` and `action_holiday_hours` registered, correct YAML list syntax (indented list under `actions:` is accepted), and valid YAML. It accepts the Level 2 domain layout (e.g. `version`, `responses`, then `actions:` with list items indented). No check for virtual environment.

```bash
#!/bin/bash
cd /home/codio/workspace/level2

score=0
max_score=11

echo "Running Lab 4.1 Assessment Checks..."
echo ""

# Check 1: domain/basics.yml exists (1 point) - file they are instructed to edit
echo "Check 1: Verifying domain file exists..."
if [ ! -f "domain/basics.yml" ]; then
    echo "❌ Check 1: FAILED - domain/basics.yml not found (0 points)"
    echo "Hint: Ensure domain/basics.yml exists"
else
    echo " Check 1: PASSED - domain/basics.yml exists (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 2: actions: section exists (2 points) - explicit in instructions
echo "Check 2: Verifying actions: section exists..."
if [ -f "domain/basics.yml" ] && grep -q "^actions:" domain/basics.yml 2>/dev/null; then
    echo " Check 2: PASSED - actions: section found (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 2: FAILED - actions: section not found (0 points)"
    echo "Hint: Add 'actions:' section to domain/basics.yml"
fi
echo ""

# Check 3: action_bank_hours is registered (2 points) - explicit
echo "Check 3: Verifying action_bank_hours is registered..."
if [ -f "domain/basics.yml" ] && grep -q "action_bank_hours" domain/basics.yml 2>/dev/null; then
    if awk '/^actions:/,/^[a-z]/ {if (/action_bank_hours/) found=1} END {exit !found}' domain/basics.yml 2>/dev/null; then
        echo " Check 3: PASSED - action_bank_hours is registered under actions: (2 points)"
        score=$((score + 2))
    else
        echo "⚠️  Check 3: PARTIAL - action_bank_hours found but may not be under actions: section (1 point)"
        score=$((score + 1))
    fi
else
    echo "❌ Check 3: FAILED - action_bank_hours not found in domain file (0 points)"
    echo "Hint: Add '- action_bank_hours' under the actions: section"
fi
echo ""

# Check 4: action_holiday_hours is registered (2 points) - explicit
echo "Check 4: Verifying action_holiday_hours is registered..."
if [ -f "domain/basics.yml" ] && grep -q "action_holiday_hours" domain/basics.yml 2>/dev/null; then
    if awk '/^actions:/,/^[a-z]/ {if (/action_holiday_hours/) found=1} END {exit !found}' domain/basics.yml 2>/dev/null; then
        echo " Check 4: PASSED - action_holiday_hours is registered under actions: (2 points)"
        score=$((score + 2))
    else
        echo "⚠️  Check 4: PARTIAL - action_holiday_hours found but may not be under actions: section (1 point)"
        score=$((score + 1))
    fi
else
    echo "❌ Check 4: FAILED - action_holiday_hours not found in domain file (0 points)"
    echo "Hint: Add '- action_holiday_hours' under the actions: section (the action you created in Lab 3.1)"
fi
echo ""

# Check 5: Correct YAML syntax / list format (2 points) - accepts indented list under actions:
echo "Check 5: Verifying YAML list syntax (dashes)..."
if [ -f "domain/basics.yml" ] && (grep -qE "^\s*-\s+action_bank_hours" domain/basics.yml 2>/dev/null && grep -qE "^\s*-\s+action_holiday_hours" domain/basics.yml 2>/dev/null); then
    echo " Check 5: PASSED - Correct YAML list syntax (dash format) (2 points)"
    score=$((score + 2))
else
    echo "⚠️  Check 5: PARTIAL - Action registered but may have syntax issues (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 6: Domain file is valid YAML (2 points) - verification: "YAML is valid"
echo "Check 6: Verifying domain file is valid YAML..."
if [ -f "domain/basics.yml" ] && python3 -c "import yaml; yaml.safe_load(open('domain/basics.yml'))" 2>/dev/null; then
    echo " Check 6: PASSED - domain/basics.yml is valid YAML (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 6: FAILED - domain/basics.yml has YAML syntax errors or file missing (0 points)"
    echo "Hint: Check YAML syntax (indentation, colons, dashes)"
fi
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo " PASS: Action registration verification complete! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
fi
echo "=========================================="
echo ""
echo "Summary: Check 1 (domain file) | Check 2 (actions:) | Check 3 (action_bank_hours) | Check 4 (action_holiday_hours) | Check 5 (syntax) | Check 6 (valid YAML)"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi
```

### Example student deliverable (for grading reference)

Students add or edit the `actions:` section in `domain/basics.yml` so it lists both actions. The Level 2 domain typically has `version`, `responses`, then `actions:` with list items indented (comments are optional). Example:

```yaml
version: "3.1"

responses:
  utter_greet:
    - text: "Hi! I'm a banking assistant. How can I help you today?"
  # ... other responses ...

actions:
  # List all custom actions here; name must match name() in actions/*.py
  - action_bank_hours
  - action_holiday_hours
```

## Assessment Setup and Configuration

1. **Navigate** to the Lab 4.1 section in the Codio Guide Editor.

2. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure each tab as follows.

   **General** – Name: *Lab 4.1: Registering Actions in the Domain*. Description: *Verify that students can register actions in the domain file (both action_bank_hours and action_holiday_hours)*. Points: `11`. Language: `Bash`.

   **Execution** – COMMAND: `bash /home/codio/workspace/.guides/secure/level2_graders/lab_4.1_grader.sh`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace/level2`.

   **Grading**
   - **Points**: `11` – Total points for this assessment.
   - **Allow partial points**: `OFF` – Single run; the script reports one pass/fail outcome, so partial credit is not used.
   - **Use maximum score**: `OFF` – No cap; the student can earn the full point value.
   - **Case insensitive**: `ON` – Output comparison ignores letter case so minor casing differences do not fail the test.
   - **Ignore white spaces**: `ON` – Extra spaces or newlines in the script output do not cause a failure.
   - **Substring match**: `ON` – Pass if the expected string appears anywhere in the output (full output need not match exactly).
   - **Test case** (one case):
     - **INPUT – Arguments**: leave empty – No command-line arguments are passed to the script.
     - **INPUT – STDIN**: leave empty – No stdin is fed to the script.
     - **Expected output**: ` PASS: Action registration verification complete!` (include the leading space) – The test passes when the script’s stdout contains this string (i.e. when all checks pass).
   - **Show expected answer**: `ALWAYS` – Students can see the required output phrase after submission.
   - **Show rationale to student**: `NEVER` (or as desired) – Controls whether the instructor rationale is shown to the student.
   - **Defined number of attempts**: `OFF` – No limit on submission attempts (or set a limit if desired).
   - **Rationale** (optional): e.g. *The grader checks that `domain/basics.yml` has an `actions:` section listing both `action_bank_hours` and `action_holiday_hours` with valid YAML.*

   **Files** – Create the grader script at `.guides/secure/level2_graders/lab_4.1_grader.sh`. In the Codio workspace terminal (from the workspace root), make it executable: `chmod +x .guides/secure/level2_graders/lab_4.1_grader.sh`.

3. **Save & Test** the assessment. Enable **Learning Analytics** if desired.

---
