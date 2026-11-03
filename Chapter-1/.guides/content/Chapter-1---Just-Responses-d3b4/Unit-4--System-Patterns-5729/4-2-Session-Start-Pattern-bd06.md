`pattern_session_start` runs automatically when a new conversation begins, before the user says anything.
 
```yaml
flows:
  pattern_session_start:
    name: pattern session start
    description: Start the conversation with a greeting
    nlu_trigger:
      - intent: session_start
    steps:
      - action: utter_greet
```
 
`nlu_trigger` activates a flow on a specific intent rather than through the Command Generator. The `session_start` intent is a built-in Rasa event that fires when a new session opens.
 
<table style="width:100%;border-collapse:collapse;margin:16px 0;"><tr style="background:transparent;border:none;"><td style="background:#ebe8fe;border:1px solid #c4baf9;border-left:3px solid #5a17ee;padding:12px 16px;line-height:1.6;color:#080327;font-size:0.9em;">❗<code>nlu_trigger</code> is the only place in this course where a flow activates on a system event rather than through the Command Generator. For everything else, the Command Generator reads <code>description:</code> to decide what to run.</td></tr></table>


```text
User opens chat
  ↓
Rasa detects new session
  ↓
pattern_session_start activates
  ↓
utter_greet runs
  ↓
User sees: "Hi! I'm a banking assistant..."
```
 
{Check It!|assessment}(multiple-choice-662755326)
 
---
 