#!/bin/bash
set -e

# Lab 6.2: Using Rasa Inspector – verify model exists and Inspector was run (log evidence)
cd /home/codio/workspace

score=0
max_score=6

echo "Running Lab 6.2 Assessment Checks..."
echo ""

# Check 0: Virtual environment exists in workspace root (1 point)
echo "Check 0: Verifying virtual environment..."
if [ ! -d ".venv" ]; then
    echo "❌ Check 0: FAILED - Virtual environment (.venv) not found in project root (0 points)"
    echo "Hint: From the project root, run 'python3.11 -m venv .venv' then 'source .venv/bin/activate'"
    exit 1
fi
source .venv/bin/activate
echo "✅ Check 0: PASSED - Virtual environment found (1 point)"
score=$((score + 1))
echo ""

cd /home/codio/workspace/chapter1

# Check 1: Model file exists (2 points)
echo "Check 1: Verifying model file exists..."
if [ ! -d "models" ] || [ -z "$(ls -A models/*.tar.gz 2>/dev/null)" ]; then
    echo "❌ Check 1: FAILED - No model file found in chapter1/models/ (0 points)"
    echo "Hint: Complete Lab 6.1 first: run 'python -m rasa train' from chapter1 with venv active"
    exit 1
fi
echo "✅ Check 1: PASSED - Model file found (2 points)"
score=$((score + 2))
echo ""

# Check 2: Inspector was run – logs/logs.out exists and contains server start (3 points)
echo "Check 2: Verifying Inspector was run (log evidence)..."
if [ ! -f "logs/logs.out" ]; then
    echo "❌ Check 2: FAILED - No logs/logs.out found (0 points)"
    echo "Hint: From chapter1 (with venv active), run 'python -m rasa inspect --debug --log-file logs/logs.out', wait for 'Starting Rasa server', then open the Rasa Inspect tab"
    exit 1
fi
if ! grep -q "Starting Rasa server\|0.0.0.0:5005\|inspect" logs/logs.out 2>/dev/null; then
    echo "❌ Check 2: FAILED - logs/logs.out does not show Inspector run (0 points)"
    echo "Hint: Run 'python -m rasa inspect --debug --log-file logs/logs.out' from chapter1 and leave it running until you see 'Starting Rasa server'"
    exit 1
fi
echo "✅ Check 2: PASSED - Inspector run detected in logs (3 points)"
score=$((score + 3))
echo ""

# Final summary
echo "=========================================="
if [ $score -eq $max_score ]; then
    echo "✅ PASS: Lab 6.2 verification complete! Score: $score/$max_score"
    echo "PASS"
    echo "Successfully passed!"
else
    echo "❌ FAIL: Score $score/$max_score - Review the failed checks above."
    echo "FAIL"
fi
echo "=========================================="
if [ $score -lt $max_score ]; then
    exit 1
fi
