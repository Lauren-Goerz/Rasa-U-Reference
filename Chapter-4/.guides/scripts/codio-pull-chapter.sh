#!/usr/bin/env bash
# Pull one chapter folder from GitHub into the Codio workspace root.
# Safe: does NOT push to GitHub. Does NOT touch other chapters on GitHub.
#
# Usage (in Codio terminal):
#   export CHAPTER_DIR=Chapter-1
#   bash scripts/codio-pull-chapter.sh
#
# Or from workspace root after copying this script:
#   CHAPTER_DIR=Chapter-1 bash codio-pull-chapter.sh

set -euo pipefail

CHAPTER_DIR="${CHAPTER_DIR:?Set CHAPTER_DIR, e.g. Chapter-1 or Setup-and-Install}"
REPO_URL="${REPO_URL:-git@github.com:RasaHQ/Rasa-University.git}"
BRANCH="${BRANCH:-main}"

cd "${CODIO_WORKSPACE:-$HOME/workspace}"

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "Initializing git in $(pwd)..."
  git init
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  git remote add origin "$REPO_URL"
else
  git remote set-url origin "$REPO_URL"
fi

echo "Fetching origin/$BRANCH..."
git fetch origin "$BRANCH"

if ! git rev-parse "origin/$BRANCH" >/dev/null 2>&1; then
  echo "Error: origin/$BRANCH not found after fetch." >&2
  exit 1
fi

if ! git cat-file -e "origin/$BRANCH:$CHAPTER_DIR" 2>/dev/null; then
  echo "Error: folder '$CHAPTER_DIR' not found on origin/$BRANCH." >&2
  echo "Valid top-level folders:" >&2
  git ls-tree --name-only "origin/$BRANCH" | grep -E '^(Chapter-|Setup-and-Install)' || true
  exit 1
fi

echo "Checking out $CHAPTER_DIR from GitHub..."
git checkout "origin/$BRANCH" -- "$CHAPTER_DIR/"

echo "Updating workspace from $CHAPTER_DIR/ (other chapters on GitHub are untouched)..."
if command -v rsync >/dev/null 2>&1; then
  rsync -a "$CHAPTER_DIR"/ ./ --delete
else
  cp -a "$CHAPTER_DIR"/. .
fi

echo "Cleaning monorepo paths from workspace only..."
rm -rf Chapter-1 Chapter-2 Chapter-3 Chapter-4 Chapter-5 Chapter-6 Setup-and-Install README.md 2>/dev/null || true

if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -m "Sync from GitHub $CHAPTER_DIR"
  echo "Committed local Codio snapshot."
else
  echo "No file changes — workspace already matches GitHub $CHAPTER_DIR."
fi

echo "Done. Publish this assignment in Codio if students should see changes."
echo "Do NOT run 'git push' from Codio unless you intend to update the GitHub monorepo."
