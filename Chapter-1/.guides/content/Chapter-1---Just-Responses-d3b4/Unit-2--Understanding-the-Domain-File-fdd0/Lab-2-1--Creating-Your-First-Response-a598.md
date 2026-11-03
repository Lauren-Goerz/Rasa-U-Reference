<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Add `utter_goodbye` to `domain/basics.yml`.
 
**1. Open the domain file**
 
Open `chapter1/domain/basics.yml`. Confirm it starts with `version: "3.1"` and has a `responses:` section with `utter_greet`, `utter_help`, and `utter_contact`.
 
**2. Add `utter_goodbye`**
 
After the last response block, add:
 
```yaml
  utter_goodbye:
    - text: "Goodbye! Have a great day!"
      metadata:
        rephrase: True
```
 
Use 2-space indentation throughout. No tabs.
 
**3. Check before saving**
 
- Response name ends with a colon.
- Each message line starts with `- text:`.
- `utter_goodbye` and `rephrase` are spelled exactly as shown.
- Use [yamlchecker.com](https://yamlchecker.com) to validate if unsure.
Your complete `responses:` section should look like:
 
```yaml
responses:
  utter_greet:
    - text: "Hi! I'm a banking assistant. How can I help you today?"
      metadata:
        rephrase: True
 
  utter_help:
    - text: |
        I can help you with:
        - Checking your balance
        - Transferring money
        - Bank hours
        - Contact information
      metadata:
        rephrase: True
 
  utter_contact:
    - text: "You can reach us at support@bank.com or call 1-800-BANK-123."
      metadata:
        rephrase: False
 
  utter_goodbye:
    - text: "Goodbye! Have a great day!"
      metadata:
        rephrase: True
```
 
{Check It!|assessment}(code-output-compare-101020002)
 
---

