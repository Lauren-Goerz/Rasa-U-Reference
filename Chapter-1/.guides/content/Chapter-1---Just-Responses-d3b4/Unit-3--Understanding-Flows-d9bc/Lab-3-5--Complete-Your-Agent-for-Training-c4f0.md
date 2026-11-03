<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Add the hours and balance flows and responses so the agent is ready to train.
 
**1. Add two responses to `domain/basics.yml`**
 
Under `responses:`, after `utter_goodbye`:
 
```yaml
  utter_hours:
    - text: "We're open Monday–Friday 9am–5pm and Saturday 9am–1pm. Closed Sundays."
      metadata:
        rephrase: True
 
  utter_balance:
    - text: "To check your balance, say 'Check my balance' and have your account number ready."
      metadata:
        rephrase: True
```
 
**2. Create `data/basics/hours.yml`**
 
```yaml
flows:
  hours:
    name: bank hours
    description: Provide bank opening hours and schedule.
    steps:
      - action: utter_hours
```
 
**3. Create `data/basics/balance.yml`**
 
```yaml
flows:
  balance:
    name: account balance help
    description: Explain how to check account balance.
    steps:
      - action: utter_balance
```

Use **Check It!** below to verify everything has been input correctly.

{Check It!|assessment}(code-output-compare-350500005)
