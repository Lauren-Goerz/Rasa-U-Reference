
<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Create `chapter3/data/basics/check_balance.yml`:
 
```yaml
flows:
  check_balance:
    name: check account balance
    description: Ask the user for their account number and return their balance.
    persisted_slots:
      - account
    steps:
      - collect: account
        description: |
          A numeric account number consisting ONLY of digits (e.g., 123456, 987654321).
          CRITICAL: Do NOT extract this slot unless the user explicitly provides numbers.
          Do NOT extract from phrases like "account balance", "check account", "my account".
          Only extract when the user says actual digits like "123456" or "my account number is 789012".
        rejections:
          - if: not (slots.account matches "^[0-9]{4,}$")
            utter: utter_invalid_account
      - action: action_check_balance_simple
```
 
| Field | What it does |
|---|---|
| `description` (flow) | Tells the LLM when to trigger this flow |
| `persisted_slots` | Carries the `account` value into the next session |
| `description` (collect) | Tells the LLM what a valid account value looks like |
| `rejections` | Checks the extracted value against a condition |
| `utter_invalid_account` | Sent when a rejection fires; `utter_ask_account` then runs again |
| `action_check_balance_simple` | Reads the slot and returns the balance |
 

{Check It!|assessment}(code-output-compare-1235165472)

---