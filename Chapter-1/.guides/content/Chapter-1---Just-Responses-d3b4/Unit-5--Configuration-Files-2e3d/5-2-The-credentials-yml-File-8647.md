<table style="width:100%;border-collapse:collapse;margin:0 0 16px;"><tr style="background:transparent;border:none;"><td style="background:#ebe8fe;border:1px solid #c4baf9;border-left:3px solid #5a17ee;padding:12px 16px;line-height:1.6;color:#080327;font-size:0.9em;"><strong>

You do not need to modify this file in this course.</strong> It is documented here so you know what it does and where to find it when you add channels later.</td></tr></table>
`credentials.yml` defines how your agent connects to chat interfaces.
 
```yaml
rest:
 
socketio:
  bot_message_evt: bot_uttered
  session_persistence: true
  user_message_evt: user_uttered
```
 
| Field | What it does |
|---|---|
| `rest` | Enables the REST API channel. Empty means use defaults. |
| `socketio` | Enables Socket.IO, used by Rasa Inspector. |
| `bot_message_evt` | Event name emitted when the agent sends a message. |
| `session_persistence` | Keeps conversation state across messages. Required for multi-turn conversations. |
| `user_message_evt` | Event name emitted when a user sends a message. |
 
To add channels (Slack, Twilio, custom), add the relevant block with its required credentials.
 
{Check It!|assessment}(multiple-choice-372693770)
 
---