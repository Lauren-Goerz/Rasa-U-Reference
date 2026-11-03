from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionBankHours(Action):
    """A simple custom action that returns bank hours."""

    def name(self) -> Text:
        return "action_bank_hours"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Our bank hours are Monday-Friday 9am-5pm, Saturday 10am-2pm. We're closed on Sundays."
        )
        return []
