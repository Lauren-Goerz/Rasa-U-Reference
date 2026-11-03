When Rasa calls `run()` on a custom action, it passes a `tracker` object containing the full conversation state, including every slot set so far. Read a slot value with:
 
```python
account = tracker.get_slot("account")
```
 
`get_slot()` returns `None` if the slot has not been set. In production, always check for it before using the value:
 
```python
account = tracker.get_slot("account")
if not account:
    dispatcher.utter_message(text="I don't have your account number.")
    return []
```
 
In the next lab, the flow guarantees the slot is set before the action runs, so the `None` check is omitted for clarity.
 
{Check It!|assessment}(multiple-choice-932698064)
 
---
