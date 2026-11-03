#!/usr/bin/env bash
# Start Rasa Inspector for Level 1.
# Usage: bash .guides/scripts/start_rasa_inspect.sh  (from workspace root)
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
[ -d level1 ] || { echo "Error: level1/ not found."; exit 1; }
[ -f .venv/bin/activate ] && source .venv/bin/activate
cd level1
mkdir -p logs
exec python -m rasa inspect --debug --log-file logs/logs.out
