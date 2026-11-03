 Take a complete agent walkthrough showing how all pieces connect:

 **Steps**
 
1. Make sure your .venv is still active, and start Inspector from `chapter1`. 

```bash
cd chapter1
python -m rasa inspect 
```
2. Open a new session: `pattern_session_start` triggers automatically. Give it a second or two to load.
3. Look at the interaction list below, try asking for help, ask for contact info, then end the conversation.
4. Watch the flow panel to see which flow activates for each message.

 
| Turn | What happens |
|---|---|
| User opens chat | `pattern_session_start` runs → `utter_greet` |
| "How do I contact support?" | Command Generator matches `contact` flow → `utter_contact` |
| "Thanks" | Flow completes → `pattern_completed` → agent waits for next input |
 
Files involved: `data/system/patterns/patterns.yml`, `domain/basics.yml`, `data/basics/*.yml`, `config.yml`.
 
