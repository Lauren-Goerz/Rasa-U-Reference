
<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Add two new slots and two new responses that can be used together in a single flow. 

Look at the `chapter4/domain/basics.yml` file in the panel to the right. The `account` slot and `utter_ask_account` response are already there from the last chapter. 
 
**Step 1.** Add `amount` and `recipient` under the existing `slots:` block:
 
```yaml
  amount:
    type: text
  recipient:
    type: text
```
 
**Step 2.** Add two ask responses under `responses:`:
 
```yaml
  utter_ask_amount:
    - text: "How much would you like to transfer?"
      metadata:
        rephrase: False
 
  utter_ask_recipient:
    - text: "Who would you like to transfer money to?"
      metadata:
        rephrase: False
```
 
**Step 3.** Add `action_process_transfer` to the `actions:` list, keeping every action already there:
 
```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
  - action_check_balance_simple
  - action_process_transfer
```
 
**Verify.** `domain/basics.yml` should now contain `amount` and `recipient` slots, both ask responses, and `action_process_transfer` under `actions:`.
 
{Check It!|assessment}(code-output-compare-401020001)
 
---