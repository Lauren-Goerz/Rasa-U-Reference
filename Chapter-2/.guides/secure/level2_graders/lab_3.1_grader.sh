#!/bin/bash
cd /home/codio/workspace/chapter2

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
