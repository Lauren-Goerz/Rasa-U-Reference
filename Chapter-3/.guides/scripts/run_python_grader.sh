#!/usr/bin/env bash
# Run a Python grader on Codio: prefer project .venv if present, else system python3.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="${CODIO_WORKSPACE:-/home/codio/workspace}"
VENV_PY="${WORKSPACE}/.venv/bin/python3"
if [[ -x "${VENV_PY}" ]]; then
  exec "${VENV_PY}" "$@"
else
  exec python3 "$@"
fi
