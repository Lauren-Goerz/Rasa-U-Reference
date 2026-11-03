The starter project includes a working action in `actions/action_bank_hours.py`. Read it alongside the annotations below.
 
```python
from datetime import datetime                    # (1)
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker             # (2)
from rasa_sdk.executor import CollectingDispatcher
 
class ActionBankHours(Action):                   # (3)
 
    def name(self) -> Text:
        return "action_bank_hours"               # (4)
 
    async def run(
        self,
        dispatcher: CollectingDispatcher,        # (5)
        tracker: Tracker,                        # (6)
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
 
        weekday = datetime.now().weekday()       # 0=Mon, 5=Sat, 6=Sun
 
        if weekday == 6:
            message = "Today is Sunday, we're closed."
        elif weekday == 5:
            message = "Today is Saturday, we're open 10am-2pm."
        else:
            message = (
                "Our bank hours are Monday-Friday 9am-5pm, "
                "Saturday 10am-2pm. We're closed on Sundays."
            )
 
        dispatcher.utter_message(text=message)   # (7)
        return []                                # (8)
```
 
| # | What it is | Why it is there |
|---|---|---|
| 1 | `from datetime import datetime` | Standard Python. Provides `datetime.now().weekday()` which returns an integer (0=Mon, 6=Sun). The weekday logic that follows is also plain Python, not Rasa-specific. |
| 2 | `from rasa_sdk import Action, Tracker` | `Action` is the base class for custom actions. `Tracker` provides access to conversation state — slots, latest message, event history. |
| 3 | `class ActionBankHours(Action)` | Subclassing `Action` defines this as a custom action. The class name is for your code only. Rasa identifies the action by what `name()` returns, not the class name. |
| 4 | `return "action_bank_hours"` | The action name used in the domain's `actions:` list. The name here and the domain entry must match exactly. |
| 5 | `dispatcher` | Used to send messages back to the user via `dispatcher.utter_message()`. |
| 6 | `tracker` | Holds conversation state. Use `tracker.get_slot()` to read slot values and `tracker.latest_message` to access what the user said. |
| 7 | `dispatcher.utter_message(text=message)` | Sends the computed string to the user. |
| 8 | `return []` | Returns no events. Pass slot update events here when you need to set memory. |
 
---
 