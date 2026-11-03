<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Have a look at the `chapter3/domain/basics.yml` file on your right. The starter file already lists `action_bank_hours` and `action_holiday_hours` under `actions:`.
 
**Step 1.** Add the `slots:` block before `responses:`:
 
```yaml
slots:
  account:
    type: text
```
 
**Step 2.** Add both ask responses under `responses:`:
 
```yaml
  utter_ask_account:
    - text: "Can you provide your account number?"
      metadata:
        rephrase: True
 
  utter_invalid_account:
    - text: "Please enter a numeric account number."
      metadata:
        rephrase: False
```
 
Rasa sends `utter_ask_account` when the `account` slot is empty at a `collect` step. `utter_invalid_account` is sent when a slot rejection fires. Both of these responses are further defined when we build the flow that uses this slot. 

Remember:`rephrase: True` allows the LLM to reword the response to fit the conversation context using the [contextual response rephraser](https://rasa.com/docs/reference/primitives/contextual-response-rephraser/). 
 
**Step 3.** Add `action_check_balance_simple` to the `actions:` list:
 
```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
  - action_check_balance_simple
```
 
**Verify.** `domain/basics.yml` should now contain:
 
- `slots:` with `account` of type `text` and mapping `from_llm`
- `utter_ask_account` with `rephrase: True`
- `utter_invalid_account` as a plain text response
- All three action names under `actions:`
{Check It!|assessment}(code-output-compare-3187585640)