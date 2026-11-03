
<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

`action_check_balance_simple` is already registered in the domain from Lab 2.1. This lab creates the Python file that implements it.
 
Create `chapter3/actions/action_check_balance_simple.py`: Paste in the copy below. 
 
```python
from typing import Any, Dict, List, Text
 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
 
 
class ActionCheckBalanceSimple(Action):
    """Reads the account slot and returns a demo balance."""
 
    def name(self) -> Text:
        return "action_check_balance_simple"
 
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        account = tracker.get_slot("account")
 
        dispatcher.utter_message(
            text=f"The balance for account {account} is $1223.45."
        )
        return []
```
 
{Check It!|assessment}(code-output-compare-2346557110)
