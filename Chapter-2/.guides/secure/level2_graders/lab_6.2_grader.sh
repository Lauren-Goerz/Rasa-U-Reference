#!/bin/bash
# Chapter 2 Lab 6.2: confirm `rasa inspect --log-file logs/logs.out` was run and the log file exists with evidence.

WORKSPACE_ROOT="${CODIO_WORKSPACE:-/home/codio/workspace}"
cd "$WORKSPACE_ROOT/chapter2" || {
    echo "❌ FAILED - chapter2/ not found under workspace root."
    exit 1
}

echo "Running Lab 6.2 Assessment Checks..."
echo ""

echo "Check 1: Verifying Inspector log file exists..."
if [ ! -f "logs/logs.out" ]; then
    echo "❌ Check 1: FAILED - chapter2/logs/logs.out not found (0 points)"
    echo "Hint: From chapter2, run: mkdir -p logs && python -m rasa inspect --debug --log-file logs/logs.out"
    exit 1
fi
echo " Check 1: PASSED - logs/logs.out exists"
echo ""

echo "Check 2: Verifying log shows Rasa Inspector started..."
if ! grep -q "Starting Rasa server\|0.0.0.0:5005\|inspect" logs/logs.out 2>/dev/null; then
    echo "❌ Check 2: FAILED - logs/logs.out does not show an Inspector run (0 points)"
    echo "Hint: Leave inspect running until the server starts; the log should mention the server or inspect."
    exit 1
fi
echo " Check 2: PASSED - Rasa Inspector run recorded in logs"
echo ""

echo "=========================================="
echo "✅ PASS: Lab 6.2 verification complete!"
echo "Successfully passed!"
echo "=========================================="
exit 0
