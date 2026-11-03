#!/bin/bash
cd /home/codio/workspace/chapter2

max_score=12
c1=0; c2=0; c3=0; c4=0; c5=0; c6=0

echo "Running Lab 5.1 Assessment Checks..."
echo ""

# Check 1: hours.yml file exists (2 points)
echo "Check 1: Verifying hours.yml flow file exists..."
if [ -f "data/basics/hours.yml" ]; then
    echo " Check 1: PASSED - hours.yml file exists (2 points)"
    c1=2
else
    echo "❌ Check 1: FAILED - data/basics/hours.yml not found (0 points)"
    echo "Hint: Create hours.yml in the data/basics/ folder"
fi
echo ""

# Check 2: hours flow exists (1 point)
echo "Check 2: Verifying hours flow exists..."
if [ -f "data/basics/hours.yml" ] && grep -q "^flows:" data/basics/hours.yml 2>/dev/null && grep -q "^  hours:" data/basics/hours.yml 2>/dev/null; then
    echo " Check 2: PASSED - hours flow found (1 point)"
    c2=1
else
    echo "❌ Check 2: FAILED - hours flow not found (0 points)"
    echo "Hint: Add 'flows:' and '  hours:' to hours.yml"
fi
echo ""

# Check 3: hours flow uses action_bank_hours (2 points)
echo "Check 3: Verifying flow uses action_bank_hours..."
if [ -f "data/basics/hours.yml" ] && grep -q "action_bank_hours" data/basics/hours.yml 2>/dev/null && grep -q "steps" data/basics/hours.yml 2>/dev/null; then
    echo " Check 3: PASSED - action_bank_hours is used in steps (2 points)"
    c3=2
else
    echo "❌ Check 3: FAILED - action_bank_hours not found in flow (0 points)"
    echo "Hint: Add '- action: action_bank_hours' under steps:"
fi
echo ""

# Check 4: holiday_hours.yml exists (2 points)
echo "Check 4: Verifying holiday_hours.yml flow file exists..."
if [ -f "data/basics/holiday_hours.yml" ]; then
    echo " Check 4: PASSED - holiday_hours.yml file exists (2 points)"
    c4=2
else
    echo "❌ Check 4: FAILED - data/basics/holiday_hours.yml not found (0 points)"
    echo "Hint: Create holiday_hours.yml in the data/basics/ folder (flow for your action from Lab 3.1)"
fi
echo ""

# Check 5: holiday_hours flow structure (2 points)
echo "Check 5: Verifying holiday_hours flow structure..."
if [ -f "data/basics/holiday_hours.yml" ] && grep -q "^flows:" data/basics/holiday_hours.yml 2>/dev/null && grep -q "holiday_hours" data/basics/holiday_hours.yml 2>/dev/null && grep -q "action_holiday_hours" data/basics/holiday_hours.yml 2>/dev/null && grep -q "steps" data/basics/holiday_hours.yml 2>/dev/null; then
    echo " Check 5: PASSED - holiday_hours flow has flows:, holiday_hours:, and uses action_holiday_hours (2 points)"
    c5=2
else
    echo "❌ Check 5: FAILED - holiday_hours.yml needs flows:, a flow named holiday_hours:, and - action: action_holiday_hours (0 points)"
    echo "Hint: Add flows: then '  holiday_hours:' with name:, description:, steps: and - action: action_holiday_hours"
fi
echo ""

# Check 6: holiday_hours has name and description (1 point)
echo "Check 6: Verifying holiday_hours flow has name and description..."
if [ -f "data/basics/holiday_hours.yml" ] && grep -q "name:" data/basics/holiday_hours.yml 2>/dev/null && grep -q "description:" data/basics/holiday_hours.yml 2>/dev/null; then
    echo " Check 6: PASSED - Flow has name and description (1 point)"
    c6=1
else
    echo "❌ Check 6: FAILED - Flow missing name or description (0 points)"
    echo "Hint: Add name: and description: to your holiday_hours flow so the LLM can match user questions"
fi
echo ""

# Set score: when all six checks pass, set 12 directly (avoids Codio arithmetic quirk)
if [ "$c1" = 2 ] && [ "$c2" = 1 ] && [ "$c3" = 2 ] && [ "$c4" = 2 ] && [ "$c5" = 2 ] && [ "$c6" = 1 ]; then
  score=12
else
  score=$(expr $c1 + $c2 + $c3 + $c4 + $c5 + $c6 2>/dev/null || echo "0")
fi

# Final summary
echo "=========================================="
if [ "$score" -eq "$max_score" ]; then
    echo " PASS: Flow creation verification complete! Score: $score/$max_score"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
fi
echo "=========================================="
echo ""
echo "Summary: Check 1-3 (hours.yml) | Check 4-6 (holiday_hours.yml)"
echo "Score: $score/$max_score"
if [ "$score" -lt "$max_score" ]; then
    exit 1
fi
