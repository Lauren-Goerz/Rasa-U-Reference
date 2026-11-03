from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProcessTransfer(Action):
    """A custom action that processes a money transfer using multiple slots."""

    def name(self) -> Text:
        return "action_process_transfer"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        amount = tracker.get_slot("amount") or ""
        recipient = (tracker.get_slot("recipient") or "")
        account = tracker.get_slot("account") or ""

        dispatcher.utter_message(text=f"Transfer of ${amount} from account {account} to {recipient} has been processed successfully.")
        return []

