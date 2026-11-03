#!/bin/bash
# Codio runs this file from .guides/startup.sh on assignment open.
# Adds source lines to ~/.bashrc so every NEW terminal loads the vars
# and activates the venv automatically.

# Block 1: Source .env (Rasa license) from workspace root
ENV_DOTENV="/home/codio/workspace/.env"
DOTENV_MARKER="# Codio .env loader (do not remove)"
BASHRC="/home/codio/.bashrc"
if ! grep -q "$DOTENV_MARKER" "$BASHRC" 2>/dev/null; then
  echo "" >> "$BASHRC"
  echo "$DOTENV_MARKER" >> "$BASHRC"
  echo "[ -f \"$ENV_DOTENV\" ] && set -a && source \"$ENV_DOTENV\" && set +a" >> "$BASHRC"
fi

# Block 2: Source secure/rasa_env (OpenAI key) from workspace
ENV_FILE="/home/codio/workspace/secure/rasa_env"
MARKER="# Codio Rasa env (do not remove)"
if ! grep -q "$MARKER" "$BASHRC" 2>/dev/null; then
  echo "" >> "$BASHRC"
  echo "$MARKER" >> "$BASHRC"
  echo "[ -f \"$ENV_FILE\" ] && source \"$ENV_FILE\"" >> "$BASHRC"
fi

# Block 3: Auto-activate .venv in every new terminal
VENV_LINE="[ -f /home/codio/workspace/.venv/bin/activate ] && source /home/codio/workspace/.venv/bin/activate"
VENV_MARKER="# Codio venv auto-activate (do not remove)"
if ! grep -q "$VENV_MARKER" "$BASHRC" 2>/dev/null; then
  echo "" >> "$BASHRC"
  echo "$VENV_MARKER" >> "$BASHRC"
  echo "$VENV_LINE" >> "$BASHRC"
fi