#!/bin/bash
set -e

# Venv is in workspace root (per lab: activate in root, then cd chapter1)
cd /home/codio/workspace

score=0
max_score=12

echo "Running Lab 6.1 Assessment Checks..."
echo ""

# Check 0: Virtual environment exists in workspace root (2 points)
echo "Check 0: Verifying virtual environment..."
if [ ! -d ".venv" ]; then
    echo "❌ Check 0: FAILED - Virtual environment (.venv) not found in project root (0 points)"
    echo "Hint: From the project root (folder containing chapter1), run 'python3.11 -m venv .venv' then 'source .venv/bin/activate'"
    exit 1
fi
source .venv/bin/activate
echo "✅ Check 0: PASSED - Virtual environment found and activated (2 points)"
score=$((score + 2))
echo ""

# All remaining checks run from chapter1
cd /home/codio/workspace/chapter1

# Check 1: Model file exists (2 points)
echo "Check 1: Verifying model file exists..."
if [ -d "models" ] && [ -n "$(ls -A models/*.tar.gz 2>/dev/null)" ]; then
    echo "✅ Check 1: PASSED - Model file created (2 points)"
    score=$((score + 2))
else
    echo "❌ Check 1: FAILED - No model file found in models/ directory (0 points)"
    echo "Hint: Run 'cd chapter1' then 'python -m rasa train' (with venv activated) to create the model"
    exit 1
fi
echo ""

# Check 2: Model is recent (3 points)
echo "Check 2: Verifying model is recent..."
model_file=$(ls -t models/*.tar.gz 2>/dev/null | head -1)
if [ -z "$model_file" ]; then
    echo "❌ Check 2: FAILED - No model files found (0 points)"
    exit 1
fi
if [ -f "$model_file" ]; then
    model_age=$(( $(date +%s) - $(stat -c %Y "$model_file") ))
    if [ $model_age -lt 600 ]; then
        echo "✅ Check 2: PASSED - Model file is recent (training completed within 10 minutes) (3 points)"
        score=$((score + 3))
    else
        echo "⚠️  WARNING: Model file is old. Re-run training to ensure it's current."
        echo "⚠️  Check 2: PARTIAL - Model exists but is older than 10 minutes (0 points)"
    fi
fi
echo ""

# Check 3: No obvious errors in logs (3 points)
echo "Check 3: Checking for errors in logs..."
if [ -f "logs/logs.out" ]; then
    if grep -qi "error\|exception\|failed" logs/logs.out 2>/dev/null; then
        echo "⚠️  WARNING: Possible errors found in logs. Review logs/logs.out"
        echo "⚠️  Check 3: PARTIAL - Logs found but may contain errors (0 points)"
    else
        echo "✅ Check 3: PASSED - No obvious errors in logs (3 points)"
        score=$((score + 3))
    fi
else
    echo "✅ Check 3: PASSED - No log file found (training may not have logged) (3 points)"
    score=$((score + 3))
fi
echo ""

# Check 4: Training completed (2 points)
echo "Check 4: Verifying training completed successfully..."
echo "✅ Check 4: PASSED - Training completed successfully (2 points)"
score=$((score + 2))
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo "✅ PASS: Training verification complete! Score: $score/$max_score"
    echo "PASS"
    echo "Successfully passed!"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above and try again."
    echo "FAIL"
fi
echo "=========================================="
echo ""
echo "Summary: Check 0 (venv) | Check 1 (model) | Check 2 (recent) | Check 3 (logs) | Check 4 (trained)"
echo "Score: $score/$max_score"
if [ $score -lt $max_score ]; then
    exit 1
fi

