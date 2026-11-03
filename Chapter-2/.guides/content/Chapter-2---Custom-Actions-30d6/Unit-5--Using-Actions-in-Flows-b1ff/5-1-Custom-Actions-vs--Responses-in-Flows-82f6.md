 
Response steps and action steps use identical syntax. Rasa tells them apart by name prefix: `utter_` calls a response, `action_` calls a Python class.
 
```yaml
steps:
  - action: utter_contact       # calls a response (chapter 1 style)
  - action: action_bank_hours   # calls Python code (chapter 2)
```
 
You can mix both types in any order. Rasa runs them sequentially:
 
```yaml
flows:
  hours_and_contact:
    name: hours and contact
    description: Tell the user bank hours and provide contact information.
    steps:
      - action: action_bank_hours   # dynamic hours
      - action: utter_contact       # static contact text
```
 
---