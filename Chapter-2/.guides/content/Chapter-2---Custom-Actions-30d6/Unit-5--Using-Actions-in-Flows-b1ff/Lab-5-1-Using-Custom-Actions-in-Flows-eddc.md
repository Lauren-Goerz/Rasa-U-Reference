<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>
Create two flow files that activate your custom actions when users ask about bank hours or holiday hours.
 
---
 
**1. Confirm your existing flows**
 
Open `data/basics/`. You should see: `greet.yml`, `help.yml`, `contact.yml`, `goodbye.yml`.
 
---
 
**2. Create the bank hours flow**
 
Create `data/basics/hours.yml`:
 
```yaml
flows:
  hours:
    name: bank hours
    description: Tell the user when the bank is open.
    steps:
      - action: action_bank_hours
```
 
---
 
**3. Create the holiday hours flow**
 
Create `data/basics/holiday_hours.yml`:
 
```yaml
flows:
  holiday_hours:
    name: holiday hours
    description: Tell the user when the bank is closed or has limited hours for holidays.
    steps:
      - action: action_holiday_hours
```
 
---
 
**4. Verify before submitting**
 
Both files should be in `data/basics/`, each with `name:`, `description:`, and a `steps:` block pointing to the correct action name. Use [yamlchecker.com](https://yamlchecker.com) if you are unsure about the syntax.
 
{Check It!|assessment}(code-output-compare-389374509)