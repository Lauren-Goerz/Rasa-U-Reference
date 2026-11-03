<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>
Confirm your virtual environment is active and you are in `chapter2/` before starting.
 
---
 
**1. Start Inspector**
 
```bash
mkdir -p logs
python -m rasa inspect --debug --log-file logs/logs.out
```
 
Leave this terminal open. Closing it stops Inspector.
 
Click **Rasa Inspect** in the top menu(blue bar above this page) to open the chat.
 
---
 
**2. Test each flow**
 
| You send | Expected flow | What should happen |
|---|---|---|
| "Hello" | `greet` | Chapter 1 greeting |
| "What are your hours?" | `hours` | Dynamic reply based on today's day |
| "Are you open on holidays?" | `holiday_hours` | Holiday schedule or closed message |
| "Help" | `help` | Chapter 1 help response |
| "How can I contact you?" | `contact` | Chapter 1 contact response |
 
---
 
**3. Use the Tracker State tab**
 
The Tracker State tab in inspector shows how Rasa interpreted each message and which action it selected. Use this when a flow does not activate as expected.
 
**If something goes wrong:**
 
- Action does not trigger: check the flow `description:`, the `actions:` list in the domain, and that the Python file exists
- Action runs but no message: confirm `dispatcher.utter_message()` is called, then check `logs/logs.out` for errors
- Python error on startup: fix the syntax and restart Inspector

{Check It!|assessment}(code-output-compare-1597644299)
 
---