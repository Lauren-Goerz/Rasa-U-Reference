**Patterns** are system flows that manage conversation lifecycle. They are configured in `data/system/patterns/patterns.yml` and run automatically when they are needed, your business flows do not need to activate or call them.
 
Two patterns matter most in Chapter 1:
 
| Pattern | Triggers when |
|---|---|
| `pattern_session_start` | A conversation begins |
| `pattern_completed` | A flow finishes successfully |
 
**All available patterns**
 
| Pattern | Triggered when |
|---|---|
| `pattern_session_start` | A conversation begins |
| `pattern_completed` | A flow finishes successfully |
| `pattern_cancelled` | A user abandons a flow mid-way |
| `pattern_clarification` | The command generator cannot confidently choose a flow |
| `pattern_correction` | A user corrects something said earlier |
| `pattern_cannot_handle` | No flow matches the user's request |
| `pattern_internal_error` | A system error occurs at runtime |
| `pattern_chitchat` | A user sends a casual or off-topic message |
| `pattern_repeat_bot_messages` | *Voice only*: a user asks the agent to repeat the last message |
| `pattern_customer_satisfaction` | A conversation ends, triggering a CSAT prompt |
 
See the [full patterns reference](https://rasa.com/docs/reference/primitives/patterns/).
 
---
 