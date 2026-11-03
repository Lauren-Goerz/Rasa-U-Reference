
All three flows you have built share a pattern: Rasa fills a slot the moment it sees a valid value, even if the user mentioned it before the flow started. Say "send $50 to Jen" and both `amount` and `recipient` fill before the first question is asked. For most slots that is the right behavior.
 
But, there is one wrinkle in this process. The `check_balance` flow uses `persisted_slots`:
 
```yaml
flows:
  check_balance:
    persisted_slots:
      - account
    steps:
      - collect: account
```
 
`persisted_slots` carries the slot value throughout the session. If `account` is already set from a previous flow, the `collect` step in `transfer_money` would be skipped entirely and whatever value was stored would go straight to the transfer action. For a slot that feeds a financial transaction, silently reusing a value is not acceptable.
 
`ask_before_filling: true` fixes this. Rasa will always pause and ask, even if the slot already has a value.
 
```yaml
- collect: account
  ask_before_filling: true
```
 
Use it sparingly. Asking when you could infer adds friction. But when a persisted slot could cause a silent wrong answer, it is the right call.
 