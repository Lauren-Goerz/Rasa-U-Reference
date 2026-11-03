 
A `collect:` step pauses the flow, sends `utter_ask_<slot_name>`, and waits for a reply. The LLM extracts a value from the user's message and stores it in the slot. The flow then moves to the next step. If the slot already has a value when the step is reached, it is skipped.
 
### Guiding the LLM with description
 
The `description` field on a `collect:` step tells the LLM what a valid value looks like. Without it, the LLM guesses from the slot name alone. A slot named `account` might match the phrase `"account number"` — a label, not an actual number.
 
```yaml
- collect: account
  description: |
    A numeric account number consisting ONLY of digits (e.g., 123456, 987654321).
    CRITICAL: Do NOT extract this slot unless the user explicitly provides numbers.
    Do NOT extract from phrases like "account balance", "check account", "my account".
    Only extract when the user says actual digits like "123456" or "my account number is 789012".
```
 
The more specific the description, the more reliably the LLM extracts the right kind of value.
 
### Catching bad values with rejections
 
The LLM can still extract a value that does not meet your requirements. A `rejections` block runs after extraction and checks the collected value itself.
 
Each rejection has two fields: `if` (a condition on the slot value) and `utter` (the response to send if the condition is true). When a rejection fires, Rasa sends the `utter` response, clears the slot, and repeats the `collect` step. For more complex validation, use a custom action instead.
 
```yaml
- collect: account
  description: |
    A numeric account number consisting ONLY of digits (e.g., 123456, 987654321).
    CRITICAL: Do NOT extract this slot unless the user explicitly provides numbers.
    Do NOT extract from phrases like "account balance", "check account", "my account".
    Only extract when the user says actual digits like "123456" or "my account number is 789012".
  rejections:
    - if: not (slots.account matches "^[0-9]{4,}$")
      utter: utter_invalid_account
```
 
This condition rejects any value that is not four or more digits. `"account number"`, `"abc123"`, and `"12"` all fail. `"48291"` passes.
 
### Persisted slots
 
By default, slots filled via collect steps are reset when a flow completes (to null or to the slot’s initial_value if one is defined).

To keep selected slot values after the flow ends, list those slots under the flow’s `persisted_slots` property (this persists them at the conversation level after the flow ends).

 
```yaml
persisted_slots:
  - account
```
 
{Check It!|assessment}(multiple-choice-2502214147)
{Check It!|assessment}(fill-in-the-blanks-1454903744)
 
---