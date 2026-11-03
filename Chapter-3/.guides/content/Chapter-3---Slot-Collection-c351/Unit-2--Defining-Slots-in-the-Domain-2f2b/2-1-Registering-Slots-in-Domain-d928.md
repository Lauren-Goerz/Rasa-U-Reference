Slots are defined in `domain/*.yml` alongside responses and actions. A slot definition alone is not enough: any slot collected from the user also needs a matching `utter_ask_<slot_name>` response, which Rasa sends when the slot is empty at a `collect` step.

```yaml
slots:
  account:
    type: text

responses:
  utter_ask_account:
    - text: "What is your account number?"
      metadata:
        rephrase: True
```

Any action the flow calls must also be listed under `actions:`. Rasa rejects unknown action names at startup.

 {Check It!|assessment}(multiple-choice-2551391875)