# Lab 3.1: Create Your Own Action

## Guide Content (For Students)

**Placement**: This lab **opens** Unit 3: Creating Your First Action (the old “3.1 Step-by-Step” page was removed; students rely on **Unit 2.1** for the `action_bank_hours` example).

---

### Your Task

Students complete a **Fill in the blanks** exercise that matches the course solution (`level3/actions/action_holiday_hours.py`), then **paste** the completed script into **`level2/actions/action_holiday_hours.py`** and run the **Code Test**. Same **fill-in → paste → Check It!** pattern as **Level 4 Lab 3.1** (`fill-in-the-blanks-401030010` → `code-output-compare-401030001`) and **Level 5 Lab 2.1**.

---

#### Fill in the blanks

**Thirteen blanks** cover imports, class, `name()`, `run()` return type, `datetime.now()`, holiday date checks, `dispatcher.utter_message`, and `return []`.

{Check It!|assessment}(fill-in-the-blanks-201030010)

---

### After the blanks — paste and Code Test

1. Create **`level2/actions/action_holiday_hours.py`** if needed.
2. Paste the completed script; save.
3. Run the grader.

{Check It!|assessment}(code-output-compare-2266471391)

---

### Quick Checklist (what the grader checks)

- [ ] **Fill in the blanks** passed (script matches course solution)
- [ ] File is under **`level2/actions/`** as **`action_holiday_hours.py`**
- [ ] Imports, `datetime`, `ActionHolidayHours`, `name()`, `run()` as in the reference solution

The **student guide page** ends with **When Rasa executes your action** (seven numbered steps + key point)—content that used to live on a separate **3.2 Understanding Action Execution** page.

---

## Assessment Setup (For Implementers)

### Overview

Students first complete a **Fill in the blanks** assessment (`.guides/assessments/fill-in-the-blanks-201030010.json`), then paste into **`level2/actions/action_holiday_hours.py`**. The **Standard Code Test** (`.guides/assessments/code-output-compare-2266471391.json`, `lab_3.2_grader.sh`) verifies the file on disk.

### Assessment Type

1. **Fill in the Blanks** — taskId **`fill-in-the-blanks-201030010`** (13 blanks; `tokens.text` uses literal `0` for each blank, sequential — same pattern as Level 4 `fill-in-the-blanks-401030010`).
2. **Standard Code Test** (Bash script) — taskId **`code-output-compare-2266471391`**

## Grader Script Location

Save the grader script at (on-disk name; matches `code-output-compare-2266471391.json`):

.guides/secure/level2_graders/lab_3.2_grader.sh

## Grader Script

The grader only checks what is explicitly instructed in the student lab: file location/name, imports, datetime, class, name(), and run().

```bash
#!/bin/bash
# Implemented as lab_3.2_grader.sh in this repo (same checks).
cd /home/codio/workspace/level2

score=0
max_score=8

echo "Running Lab 3.1 Assessment Checks..."
echo ""

# Check 1: action_holiday_hours.py file exists (2 points) - Step 1: create file in actions/
echo "Check 1: Verifying action_holiday_hours.py exists..."
if [ ! -f "actions/action_holiday_hours.py" ]; then
    echo "❌ Check 1: FAILED - actions/action_holiday_hours.py not found (0 points)"
    echo "Hint: Create the action file in the actions/ folder"
else
    echo " Check 1: PASSED - action_holiday_hours.py file exists (2 points)"
    score=$((score + 2))
fi
echo ""

# Check 2: Action file has correct imports (2 points) - Step 2
echo "Check 2: Verifying action file imports..."
if [ -f "actions/action_holiday_hours.py" ] && grep -q "from rasa_sdk import Action" actions/action_holiday_hours.py 2>/dev/null && grep -q "from rasa_sdk.executor import CollectingDispatcher" actions/action_holiday_hours.py 2>/dev/null; then
    echo " Check 2: PASSED - Correct imports found (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 2: FAILED - Missing required imports (0 points)"
    echo "Hint: Import Action from rasa_sdk and CollectingDispatcher from rasa_sdk.executor"
fi
echo ""

# Check 3: Action uses datetime for date-based logic (1 point) - Step 2
echo "Check 3: Verifying date-based logic (datetime)..."
if [ -f "actions/action_holiday_hours.py" ] && grep -q "datetime" actions/action_holiday_hours.py 2>/dev/null; then
    echo " Check 3: PASSED - datetime used for date-based message (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 3: FAILED - Action should use datetime to check if today is a holiday (0 points)"
    echo "Hint: Import datetime and use datetime.now() with .month and .day to choose your message"
fi
echo ""

# Check 4: Action class inherits from Action (1 point) - Step 3
echo "Check 4: Verifying Action class structure..."
if [ -f "actions/action_holiday_hours.py" ] && grep -q "class ActionHolidayHours(Action)" actions/action_holiday_hours.py 2>/dev/null; then
    echo " Check 4: PASSED - ActionHolidayHours class inherits from Action (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 4: FAILED - ActionHolidayHours class not found or doesn't inherit from Action (0 points)"
    echo "Hint: Class should be 'class ActionHolidayHours(Action):'"
fi
echo ""

# Check 5: name() method exists and returns correct value (1 point) - Step 4
echo "Check 5: Verifying name() method..."
if [ -f "actions/action_holiday_hours.py" ] && grep -q "def name" actions/action_holiday_hours.py 2>/dev/null && grep -q "return \"action_holiday_hours\"" actions/action_holiday_hours.py 2>/dev/null; then
    echo " Check 5: PASSED - name() method exists and returns 'action_holiday_hours' (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 5: FAILED - name() method missing or incorrect return value (0 points)"
    echo "Hint: name() method should return 'action_holiday_hours'"
fi
echo ""

# Check 6: run() method exists, uses dispatcher.utter_message, and returns [] (1 point) - Step 5
echo "Check 6: Verifying run() method and message sending..."
if [ -f "actions/action_holiday_hours.py" ] && grep -q "def run" actions/action_holiday_hours.py 2>/dev/null && grep -q "dispatcher.utter_message" actions/action_holiday_hours.py 2>/dev/null && grep -q 'return \[\]' actions/action_holiday_hours.py 2>/dev/null; then
    echo " Check 6: PASSED - run() method exists, uses dispatcher.utter_message(), and returns [] (1 point)"
    score=$((score + 1))
else
    echo "❌ Check 6: FAILED - run() must call dispatcher.utter_message() and return [] (0 points)"
    echo "Hint: run() must call dispatcher.utter_message() to send a message and return [] at the end"
fi
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo " PASS: Action creation verification complete! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
fi
echo "=========================================="
echo ""
echo "Summary: Check 1 (action file) | Check 2 (imports) | Check 3 (datetime) | Check 4 (class) | Check 5 (name()) | Check 6 (run())"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi
```

### Example student deliverable (for grading reference)

Students should produce a file at `actions/action_holiday_hours.py`. The following is a minimal example that satisfies the grader (exact wording of messages may vary):

```python
from datetime import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHolidayHours(Action):
    def name(self):
        return "action_holiday_hours"

    def run(self, dispatcher, tracker, domain):
        now = datetime.now()
        if (now.month == 1 and now.day == 1):
            message = "We're closed today for New Year's Day."
        elif (now.month == 7 and now.day == 4):
            message = "We're closed today for Independence Day."
        elif (now.month == 12 and now.day == 25):
            message = "We're closed today for Christmas."
        else:
            message = (
                "We're closed on New Year's Day, Independence Day, and Christmas. "
                "On other holidays we may have limited hours, please call ahead."
            )
        dispatcher.utter_message(text=message)
        return []
```

## Assessment Setup and Configuration

1. **Create the page** – New Codio Guide page **Lab 3.1: Create Your Own Action** (standalone: folder tree, guide editor, terminal). Add the **Guide Content** section above as the page content.

2. **Add Fill in the Blanks** – Import or create **`fill-in-the-blanks-201030010`** from `.guides/assessments/`. Points: **5**. Max attempts: **1** (or as configured in JSON). Place it **before** the Code Test on the guide page.

3. **Add Code Test** – Add Code Test → **Standard Code Test**. Configure each tab as follows.

   **General** – Name: *Lab 3.1: Create Your Own Action*. Description: *Verify that students can create action_holiday_hours.py with correct structure and date-based logic*. Points: `8`. Language: `Bash`.

   **Execution** – COMMAND: `bash /home/codio/workspace/.guides/secure/level2_graders/lab_3.2_grader.sh`. TIMEOUT: `60` seconds. Working Directory: `/home/codio/workspace/level2`.

   **Grading**
   - **Points**: `8` – Total points for this assessment.
   - **Allow partial points**: `OFF` – Single run; the script reports one pass/fail outcome, so partial credit is not used.
   - **Use maximum score**: `OFF` – No cap; the student can earn the full point value.
   - **Case insensitive**: `ON` – Output comparison ignores letter case so minor casing differences do not fail the test.
   - **Ignore white spaces**: `ON` – Extra spaces or newlines in the script output do not cause a failure.
   - **Substring match**: `ON` – Pass if the expected string appears anywhere in the output (full output need not match exactly).
   - **Test case** (one case):
     - **INPUT – Arguments**: leave empty – No command-line arguments are passed to the script.
     - **INPUT – STDIN**: leave empty – No stdin is fed to the script.
     - **Expected output**: ` PASS: Action creation verification complete!` (include the leading space) – The test passes when the script's stdout contains this string (i.e. when all checks pass).
   - **Show expected answer**: `ALWAYS` – Students can see the required output phrase after submission.
   - **Show rationale to student**: `NEVER` (or as desired) – Controls whether the instructor rationale is shown to the student.
   - **Defined number of attempts**: `OFF` – No limit on submission attempts (or set a limit if desired).
   - **Rationale** (optional): e.g. *The grader checks only what the lab instructs: action file in actions/, correct imports (including datetime), class ActionHolidayHours(Action), name() returning 'action_holiday_hours', and run() calling dispatcher.utter_message() and returning [].*

   **Files** – Grader script at `.guides/secure/level2_graders/lab_3.2_grader.sh`. In the Codio workspace terminal (from the workspace root), make it executable: `chmod +x .guides/secure/level2_graders/lab_3.2_grader.sh`.

4. **Save & Test** both assessments. Enable **Learning Analytics** if desired.

---
