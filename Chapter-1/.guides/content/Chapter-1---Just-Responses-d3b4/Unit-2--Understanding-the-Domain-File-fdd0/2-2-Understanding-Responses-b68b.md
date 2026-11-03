A **response** is a predefined message the agent can send. Responses live in `domain/basics.yml` and are referenced by name in flows.
 
```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
    metadata:
      rephrase: True
```
 
| Part | What it does |
|---|---|
| `utter_greet` | The response name. The `utter_` prefix is a Rasa convention. Flows call this name to trigger the message. |
| `- text: "..."` | The dash marks a list item. A single response can have multiple `text` entries; Rasa picks one at random. |
| `rephrase: True` | Tells the LLM to rephrase the wording while keeping the meaning, via the [contextual response rephraser](https://rasa.com/docs/reference/primitives/contextual-response-rephraser/). Without it, the agent repeats the same string every time. |
 
**When to use `rephrase: False`**
 
If `rephrase_all: true` is set globally in `endpoints.yml`, pin specific responses to exact wording with `rephrase: False`:
 
- Email addresses and phone numbers
- Account numbers, reference codes, or IDs
- Legal disclaimers or policy wording
- Specific amounts, dates, or times
<table style="width:100%;border-collapse:collapse;margin:16px 0;"><tr style="background:transparent;border:none;"><td style="background:#ebe8fe;border:1px solid #c4baf9;border-left:3px solid #5a17ee;padding:12px 16px;line-height:1.6;color:#080327;font-size:0.9em;"><code>utter_contact</code> in this project uses <code>rephrase: False</code> so the support email and phone number stay literal. Use <code>rephrase: False</code> any time exact wording is required: contact details, account numbers, legal disclaimers, specific amounts or dates.</td></tr></table>

**Multiple variations**
 
You can also list several `text` entries to add variety without using an LLM, these will then be activated in a random order. 
 
```yaml
utter_greet:
  - text: "Hi! I'm a banking assistant. How can I help you today?"
  - text: "Hello! How can I help you?"
  - text: "Welcome! I'm here to assist you."
```
 
Combine multiple entries with `rephrase: True` on each for maximum variation.
 
{Check It!|assessment}(multiple-choice-2055505786)



---
