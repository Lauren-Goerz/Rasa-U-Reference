A **flow** is a conversational path the agent runs from start to finish. It encodes the business logic for a single process: an ordered plan for what to do when that process applies.
 
Flows sit at the guided end of the autonomy spectrum. Use them when the steps are known in advance, order matters, and the language model should not invent the sequence.
 
**Flow structure**
 
```yaml
flows:
  greet:                        # Flow ID — unique, lowercase
    name: say hello             # Optional human-readable label
    description: Greet the user when they start a conversation
    steps:
      - action: utter_greet     # Calls the response from domain/basics.yml
```
 
Rasa uses a central system prompt called the **command generator** to determine the next best action at each point in a conversation. In some cases, that action is to activate a flow.

The command generator decides whether to activate a flow by reading the flow’s description: field (and its name: field, if present; otherwise it uses the flow ID). If the flow appears relevant to the user’s current need, the command generator may activate it.

Because of this, clear and specific descriptions are important. If a flow description is vague or missing, the flow may not activate reliably when it should.

We’ll cover the command generator in more detail in Unit 3.2.

 
<table style="width:100%;border-collapse:collapse;margin:16px 0;"><tr style="background:transparent;border:none;"><td style="background:#ebe8fe;border:1px solid #c4baf9;border-left:3px solid #5a17ee;padding:12px 16px;line-height:1.6;color:#080327;font-size:0.9em;"><strong><code>description:</code> is the most important field in a flow.</strong> The LLM reads it to decide when to activate the flow. If a flow is not activating when you expect it to, it is worth trying to adjust the description before trying anything else. </td></tr></table>

**Flows live in** `data/basics/*.yml`. One file per flow, or several related flows in the same file.
 
**Execution**
 
```text
User says "hello"
  ↓
Flow greet activates
  ↓
Step 1: utter_greet
  ↓
Agent responds: "Hi! I'm a banking assistant..."
  ↓
Flow completes
```
 
---