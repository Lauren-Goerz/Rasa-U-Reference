The **Command Generator** is the component that decides which flow to run. On every turn it reads the user's message, the full conversation context, and your flow descriptions, then outputs a command like `StartFlow("greet")`.
 
```text
User sends a message
  ↓
Command Generator reads:
  - the message
  - active flows and filled slots
  - conversation history
  - all flow descriptions
  ↓
Selects the next best step(s)
  ↓
Outputs: StartFlow("greet")
```
 
This makes `description:` one of the most important fields in a flow. If it is vague or missing, the correct flow may never run, even if everything else is configured correctly.
 
---
 
**What makes a description work**
 
Write the **situation**, not the action. The Command Generator needs to know *when* a flow applies, not just *what* it does.
 
| Description | Why it fails or works |
|---|---|
| `Say hello` | Describes the action, not the trigger |
| `Help user` | Too vague, every flow could claim this |
| `Respond only when the user types hello exactly` | Too narrow, misses "hi", "hey", "good morning" |
| `Greet the user when they start a conversation` | Names the situation clearly, works |
 
**Tips for writing descriptions:**
- Use action verbs and name the situation: *when the user asks for X*, *when the conversation starts*
- Use plain, standard language, avoid jargon the LLM might interpret differently
- Spell out brand names or specialised terms
- Be specific enough to exclude flows that should not activate, but broad enough to match natural variation
<table style="width:100%;border-collapse:collapse;margin:16px 0;"><tr style="background:transparent;border:none;"><td style="background:#fff9ed;border:1px solid #ffd594;border-left:3px solid #f59e0b;padding:12px 16px;line-height:1.6;color:#080327;font-size:0.9em;">If a flow is not activating when expected, the description is the first thing to check and adjust.</td></tr></table>

This course uses the [SearchReadyLLMCommandGenerator](https://rasa.com/docs/reference/config/components/llm-command-generators/#searchreadyllmcommandgenerator). See the [full docs](https://rasa.com/docs/reference/config/components/llm-command-generators/) to customise the underlying prompt.

---
