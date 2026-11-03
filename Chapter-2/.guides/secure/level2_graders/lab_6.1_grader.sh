#!/bin/bash
cd /home/codio/workspace/chapter2

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
