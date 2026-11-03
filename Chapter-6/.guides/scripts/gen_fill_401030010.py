"""One-off generator for fill-in-the-blanks-401030010.json — run from repo root."""
import json
from pathlib import Path

blanks = [
    "Any, Dict, List, Text",
    "Action",
    "action_process_transfer",
    "List[Dict[Text, Any]]",
    'tracker.get_slot("amount") or ""',
    'tracker.get_slot("recipient") or ""',
    'tracker.get_slot("account_from") or ""',
    "amount in placeholder_values or recipient in placeholder_values or account_from in placeholder_values",
    '"Please provide a real amount, recipient, and source account."',
    "[]",
    'f"Transfer of ${amount} from account {account_from} to {recipient} processed."',
    "[]",
]

parts = [
    "Complete the action that reads the three transfer slots (`amount`, `recipient`, `account_from`), re-prompts when any value is a placeholder, and otherwise sends a demo transfer confirmation:\n\n```python\nfrom typing import ",
    0,
    "\n\nfrom rasa_sdk import Action, Tracker\nfrom rasa_sdk.executor import CollectingDispatcher\n\n\nclass ActionProcessTransfer(",
    1,
    '):\n    """A custom action that processes a transfer using amount, recipient, and account_from slots.\n\n    - Reads the amount, recipient, and account_from slots from conversation memory\n    - Re-prompts if any slot is missing or contains a placeholder\n    - Otherwise sends a demo transfer confirmation\n    """\n\n    def name(self) -> Text:\n        return "',
    2,
    '"\n\n    def run(\n        self,\n        dispatcher: CollectingDispatcher,\n        tracker: Tracker,\n        domain: Dict[Text, Any],\n    ) -> ',
    3,
    ":\n        # Read the three slots (or empty string if not set)\n        amount = ",
    4,
    "\n        recipient = ",
    5,
    "\n        account_from = ",
    6,
    '\n\n        # Values that are not real—we re-ask if any slot has one of these\n        placeholder_values = ["amount", "recipient", "account number", "user_account_number", ""]\n        if ',
    7,
    ":\n            dispatcher.utter_message(text=",
    8,
    ")\n            return ",
    9,
    "\n\n        # Otherwise send the demo transfer confirmation\n        dispatcher.utter_message(text=",
    10,
    ")\n        return ",
    11,
    "\n```",
]

# Build main_text from blanks using <<<>>> syntax
main_text = parts[0]
for i in range(1, len(parts), 2):
    idx = parts[i]
    main_text += "<<<" + blanks[idx] + ">>>" + parts[i + 1]

obj = {
    "type": "fill-in-the-blanks",
    "taskId": "fill-in-the-blanks-401030010",
    "source": {
        "name": "Lab 3.1: Complete action_process_transfer (multiple slots & placeholders)",
        "showName": False,
        "instructions": "**Fill in the blanks to complete the action file.** This is the same script you will copy into `level4/actions/action_process_transfer.py` for the code assessment. Use exact names from your domain and the patterns you learned in Unit 3.1 for reading slots, `placeholder_values`, and the confirmation **f-string**.",
        "showValues": True,
        "text": main_text,
        "distractors": 'Any, Dict, Text\nList[Dict[Any, Any]]\nActionExecutor\nActionProcessTransfer\nsession\nget_latest_entity\n"account"\n"amount"\naccount in placeholder_values\nutter_ask_amount\n{}\nreturn\nTransfer done.',
        "metadata": {
            "tags": [{"name": "Assessment Type", "value": "Fill in the Blanks"}],
            "files": [],
            "opened": [{"type": "terminal", "panelNumber": 1}],
        },
        "bloomsObjectiveLevel": "",
        "learningObjectives": "",
        "guidance": """The correct answers are:

* **Any, Dict, List, Text** - Typing names for `run()` signature and return type (same pattern as Level 2 and Level 3 Lab 4.1).
* **Action** - Base class from `rasa_sdk` that `ActionProcessTransfer` subclasses.
* **action_process_transfer** - String returned by `name()`; must match `actions:` in the domain (Lab 2.1) and the `transfer_money` flow.
* **List[Dict[Text, Any]]** - Return type of `run()`.
* **tracker.get_slot("amount") or ""** - Same pattern for `recipient` and `account_from` (Unit 3.1).
* **tracker.get_slot("recipient") or ""** - Reads the recipient slot.
* **tracker.get_slot("account_from") or ""** - Reads the source account slot.
* **amount in placeholder_values or recipient in placeholder_values or account_from in placeholder_values** - True when any slot is still a placeholder (see Unit 3.1 example).
* **"Please provide a real amount, recipient, and source account."** - Message when re-prompting (`text=`).
* **[]** - Empty event list after re-prompt (first branch).
* **f\"Transfer of ${amount} from account {account_from} to {recipient} processed.\"** - Confirmation `text=` when slots look valid.
* **[]** - Empty event list after confirmation (second branch).

After this exercise, paste the **completed** script into `level4/actions/action_process_transfer.py` and run the **Code Test** assessment.""",
        "showGuidanceAfterResponseOption": {"type": "Attempts", "passedFrom": 1},
        "maxAttemptsCount": 1,
        "showExpectedAnswerOption": {"type": "Always"},
        "points": 5,
        "arePartialPointsAllowed": False,
        "useMaximumScore": False,
        "tokens": {
            "blank": blanks,
            # Codio format: every blank slot in `text` is the literal 0 (sequential blanks), matching Lab 4.1 fill-in-the-blanks-2346557111.json
            "text": [p if isinstance(p, str) else 0 for p in parts],
            "regexPositions": [],
        },
    },
}

root = Path(__file__).resolve().parents[1]
out = root / "assessments" / "fill-in-the-blanks-401030010.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(obj, f, indent="\t", ensure_ascii=False)
print("Wrote", out)
