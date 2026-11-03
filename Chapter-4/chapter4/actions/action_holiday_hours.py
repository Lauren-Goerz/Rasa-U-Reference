from datetime import datetime
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHolidayHours(Action):
    """Returns the bank's holiday schedule based on today's date."""

    def name(self) -> Text:
        return "action_holiday_hours"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        now = datetime.now()
        if now.month == 1 and now.day == 1:
            message = "We're closed today for New Year's Day."
        elif now.month == 7 and now.day == 4:
            message = "We're closed today for Independence Day."
        elif now.month == 12 and now.day == 25:
            message = "We're closed today for Christmas."
        else:
            message = (
                "We're closed on New Year's Day, Independence Day, and Christmas. "
                "On other holidays we may have limited hours—please call ahead."
            )
        dispatcher.utter_message(text=message)
        return []
