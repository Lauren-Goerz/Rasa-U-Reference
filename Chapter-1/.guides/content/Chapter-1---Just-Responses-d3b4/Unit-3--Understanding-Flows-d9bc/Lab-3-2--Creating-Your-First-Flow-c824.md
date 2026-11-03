<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Create `goodbye.yml` flow using the `utter_goodbye` response from the prior lab.
 
**1. Create the file**
 
In `data/basics/`, create a new file named exactly `goodbye.yml`. Here are some common file naming conventions:
- Lowercase only
- Underscores for multi-word names (e.g. `check_balance.yml`)
- `.yml` extension, not `.yaml`

**2. Add the flow**
 
```yaml
flows:
  goodbye:
    name: say goodbye
    description: Farewell the user when they end the conversation.
    steps:
      - action: utter_goodbye
```
 
| Field | What it does |
|---|---|
| `flows:` | Top-level key. Tells Rasa this file contains flow definitions. |
| `goodbye:` | Flow ID. Alphanumeric, underscores, and hyphens only. |
| `name:` | Human-readable label for logs. Does not affect routing. |
| `description:` | The Command Generator reads this to decide when to start the flow. |
| `steps:` | Ordered list of actions the flow executes. |
| `- action: utter_goodbye` | Calls the response from `domain/basics.yml`. Spelling must match exactly. |
 
**3. Save and verify**. Use the check below to make sure everything is formatted well. 
 

{Check It!|assessment}(code-output-compare-303200002)

---

