<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>
Add both custom actions to the domain so Rasa can call them.
 
---
 
**1. Open the domain file**
 
Open `chapter2/domain/basics.yml`. You will see the responses from the prior chapter. There is no `actions:` section yet.
 
---
 
**2. Add the `actions:` section**
 
Add the following block at the top chapter of the file, at the same indentation as `responses:`:
 
```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
```
 
---
 
**3. Check your work**
 
- `actions:` must be at the same indentation chapter as `responses:`, not nested inside it
- Each name here should correspond to what the action's `name()` method returns, this is how Rasa knows which code to call
---
 
**4. Run the assessment**
 
{Check It!|assessment}(code-output-compare-1451983168)