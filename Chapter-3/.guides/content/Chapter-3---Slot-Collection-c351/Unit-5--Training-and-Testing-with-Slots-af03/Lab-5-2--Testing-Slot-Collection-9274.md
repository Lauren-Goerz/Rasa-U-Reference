 
<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Make sure you have a trained model in `chapter3/models/` before starting.
 
If the venv is not active:
 
```bash
source .venv/bin/activate
cd chapter3
```
 
Then start Inspector:
 
```bash
python -m rasa inspect 
```
 
Click the **Rasa Inspect** button in the menu above to open Inspector.
 
**Slot collection.** Type `Check my balance`. The agent should ask for your account number. Type `1234`. The agent should respond with a balance for that account.
 
**Slot persistence.** Type `What's my balance?` again. The agent should use `1234` without asking again.
 
**Previous flows.** Type `What are your hours?` and `Hello` to confirm chapter 1 and 2 flows still work.
 
Use the debug panel to watch the `account` slot being set and reused across turns.
 
{Check It!|assessment}(multiple-choice-2446085116)
{Check It!|assessment}(multiple-choice-3751028362)
{Check It!|assessment}(multiple-choice-2697467428)
 
---