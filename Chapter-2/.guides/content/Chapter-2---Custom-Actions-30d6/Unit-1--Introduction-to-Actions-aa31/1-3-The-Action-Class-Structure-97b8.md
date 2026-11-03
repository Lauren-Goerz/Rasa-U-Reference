In this course, custom actions are Python classes that subclass `rasa_sdk.Action`. Rasa also supports implementing the action server webhook API directly for other languages, but the SDK is the standard approach.
 
```python
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, Dict, Any, List
 
class ActionBankHours(Action):
 
    def name(self) -> Text:
        return "action_bank_hours"          # must match the domain
 
    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="We're open 9am-5pm weekdays.")
        return []                            # no events to apply
```
 
- **`class ActionBankHours(Action)`** — subclassing `Action` is how you define a custom action in the SDK. The class name is for your reference only.
- **`name()`** — returns the action name used in the domain. Rasa calls whichever action has the matching name.
- **`async def run()`** — executes side effects and returns a list of events. The canonical signature is async.
- **`dispatcher.utter_message()`** — sends messages back to the user. Not returned as events.
- **`return []`** — valid when there are no events to apply. Pass slot update events here when working with memory.

> The string returned by `name()` must match the entry in your domain's `actions:` list. A mismatch means the action cannot be found.
 