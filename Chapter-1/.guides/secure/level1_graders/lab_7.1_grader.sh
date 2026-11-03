#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
CHAPTER1_DIR="$ROOT_DIR/chapter1"
DOMAIN_FILE="$CHAPTER1_DIR/domain/basics.yml"
BASICS_DATA_DIR="$CHAPTER1_DIR/data/basics"

fail() {
  echo "FAIL: $1"
  exit 1
}

[[ -d "$CHAPTER1_DIR" ]] || fail "Could not find chapter1 folder at $CHAPTER1_DIR"
[[ -f "$DOMAIN_FILE" ]] || fail "Missing domain file: chapter1/domain/basics.yml"
[[ -d "$BASICS_DATA_DIR" ]] || fail "Missing flows folder: chapter1/data/basics/"

# Lab 7.1 asks for a NEW response + a NEW flow file. We look for a flow file
# in data/basics that is not one of the earlier lab files (including hours/balance from Lab 3.5).
known_files=(
  "greet.yml"
  "help.yml"
  "contact.yml"
  "goodbye.yml"
  "hours.yml"
  "balance.yml"
  "check_balance.yml"
)

is_known() {
  local name="$1"
  for k in "${known_files[@]}"; do
    [[ "$name" == "$k" ]] && return 0
  done
  return 1
}

shopt -s nullglob
candidate_flows=()
for f in "$BASICS_DATA_DIR"/*.yml; do
  base="$(basename "$f")"
  if ! is_known "$base"; then
    candidate_flows+=("$f")
  fi
done
shopt -u nullglob

(( ${#candidate_flows[@]} > 0 )) || fail "No new flow file found in chapter1/data/basics/. Create a new .yml flow file (not greet/help/contact/goodbye/hours/balance)."

flow_file="${candidate_flows[0]}"

# Basic structure checks.
grep -Eq '^[[:space:]]*flows:' "$flow_file" || fail "Flow file $(basename "$flow_file") is missing a top-level 'flows:' key."
grep -Eq '^[[:space:]]+name:' "$flow_file" || fail "Flow file $(basename "$flow_file") is missing a 'name:' field."
grep -Eq '^[[:space:]]+description:' "$flow_file" || fail "Flow file $(basename "$flow_file") is missing a 'description:' field."

# Extract first utter_* action referenced in the flow.
utter_action="$(
  grep -Eo 'action:[[:space:]]*utter_[A-Za-z0-9_]+' "$flow_file" \
    | head -n 1 \
    | sed -E 's/.*(utter_[A-Za-z0-9_]+).*/\1/'
)"

[[ -n "${utter_action:-}" ]] || fail "Flow file $(basename "$flow_file") does not reference any 'utter_*' action."

# Ensure the response exists in the domain.
grep -Eq "^[[:space:]]*$utter_action[[:space:]]*:" "$DOMAIN_FILE" || fail "Domain is missing response '$utter_action:' in chapter1/domain/basics.yml"

echo "Checks passed:" >&2
echo "  ✓ chapter1/ folder and domain/basics.yml present" >&2
echo "  ✓ chapter1/data/basics/ contains a new flow file (not greet/help/contact/goodbye/hours/balance)" >&2
echo "  ✓ New flow has flows:, name:, description:, and at least one utter_* action" >&2
echo "  ✓ Referenced response ($utter_action) exists in domain/basics.yml" >&2
echo "Successfully passed!"
