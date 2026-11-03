#!/bin/bash
cd /home/codio/workspace/chapter2

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

# Check 3: action_bank_hours is registered (2 points) - must appear after "actions:" line
echo "Check 3: Verifying action_bank_hours is registered..."
if [ -f "domain/basics.yml" ] && grep -q "action_bank_hours" domain/basics.yml 2>/dev/null; then
    if awk '/^actions:/{seen=1} seen && /action_bank_hours/{found=1} END{exit !found}' domain/basics.yml 2>/dev/null; then
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

# Check 4: action_holiday_hours is registered (2 points) - must appear after "actions:" line
echo "Check 4: Verifying action_holiday_hours is registered..."
if [ -f "domain/basics.yml" ] && grep -q "action_holiday_hours" domain/basics.yml 2>/dev/null; then
    if awk '/^actions:/{seen=1} seen && /action_holiday_hours/{found=1} END{exit !found}' domain/basics.yml 2>/dev/null; then
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

# Check 5: Correct YAML syntax / list format (2 points) - verification: "correct indentation and dashes"
# Accept both "  - action_bank_hours" (indented under actions:) and "- action_bank_hours" (no indent)
echo "Check 5: Verifying YAML list syntax (dashes)..."
if [ -f "domain/basics.yml" ] && (grep -qE "^\s*-\s+action_bank_hours" domain/basics.yml 2>/dev/null && grep -qE "^\s*-\s+action_holiday_hours" domain/basics.yml 2>/dev/null); then
    echo " Check 5: PASSED - Correct YAML list syntax (dash format) (2 points)"
    score=$((score + 2))
else
    echo "⚠️  Check 5: PARTIAL - Action registered but may have syntax issues (1 point)"
    score=$((score + 1))
fi
echo ""

# Check 6: Domain file is valid YAML (2 points) - use absolute path; tolerate missing PyYAML
echo "Check 6: Verifying domain file is valid YAML..."
DOMAIN_ABS="/home/codio/workspace/chapter2/domain/basics.yml"
if [ -f "$DOMAIN_ABS" ] || [ -f "domain/basics.yml" ]; then
    [ -f "$DOMAIN_ABS" ] && path="$DOMAIN_ABS" || path="domain/basics.yml"
    if python3 -c "
import sys
path = '''$path'''
try:
    import yaml
except ImportError:
    sys.exit(0)
for enc in ('utf-8-sig', 'utf-8'):
    try:
        with open(path, encoding=enc) as f:
            yaml.safe_load(f)
        sys.exit(0)
    except Exception:
        pass
sys.exit(1)
" 2>/dev/null; then
        echo " Check 6: PASSED - domain/basics.yml is valid YAML (2 points)"
        score=$((score + 2))
    else
        echo "❌ Check 6: FAILED - domain/basics.yml has YAML syntax errors or file missing (0 points)"
        echo "Hint: Check YAML syntax (indentation, colons, dashes); avoid tabs; use spaces"
    fi
else
    echo "❌ Check 6: FAILED - domain/basics.yml not found (0 points)"
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
