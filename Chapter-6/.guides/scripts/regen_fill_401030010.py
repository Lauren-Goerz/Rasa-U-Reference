"""
Regenerate `.guides/assessments/fill-in-the-blanks-401030010.json` from the Level 4
`action_process_transfer` pattern (including recipient [:100]).
Run from repo root: `python .guides/scripts/regen_fill_401030010.py`
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "assessments" / "fill-in-the-blanks-401030010.json"

blanks = [
    "Any, Dict, List, Text",
    "Action",
    "action_process_transfer",
    "List[Dict[Text, Any]]",
    'tracker.get_slot("amount") or ""',
    '(tracker.get_slot("recipient") or "")[:100]',
    'tracker.get_slot("account_from") or ""',
    "amount.lower() in [p.lower() for p in placeholder_values] or recipient.lower() in [p.lower() for p in placeholder_values] or account_from.lower() in [p.lower() for p in placeholder_values]",
    '"I need the actual amount, recipient, and source account. Please provide real values."',
    "[]",
    'f"(Demo) Transfer of ${amount} from account {account_from} to {recipient} has been processed successfully."',
    "[]",
]

# Codio: same as Level 3 Lab 4.1 (fill-in-the-blanks-2346557111) — every blank uses
# literal 0 in tokens.text (sequential blanks), not 0..n index references.
parts = [
    "Complete the action that reads the three transfer slots (`amount`, `recipient`, `account_from`), "
    "caps `recipient` at 100 characters, re-prompts when any value is a placeholder, and otherwise sends "
    "a demo transfer confirmation:\n\n```python\nfrom typing import ",
    0,
    "\n\nfrom rasa_sdk import Action, Tracker\nfrom rasa_sdk.executor import CollectingDispatcher\n\n\n"
    "class ActionProcessTransfer(",
    0,
    '):\n    """A custom action that processes a money transfer using multiple slots."""\n\n'
    "    def name(self) -> Text:\n        return \"",
    0,
    '"\n\n    def run(\n        self,\n        dispatcher: CollectingDispatcher,\n        tracker: Tracker,\n'
    "        domain: Dict[Text, Any],\n    ) -> ",
    0,
    ":\n        amount = ",
    0,
    "\n        recipient = ",
    0,
    "\n        account_from = ",
    0,
    '\n\n        placeholder_values = ["amount", "recipient", "account number", "user_account_number", ""]\n        if ',
    0,
    ":\n            dispatcher.utter_message(text=",
    0,
    ")\n            return ",
    0,
    "\n\n        dispatcher.utter_message(text=",
    0,
    ")\n        return ",
    0,
    "\n```",
]

with open(path, encoding="utf-8") as f:
    data = json.load(f)

src = data["source"]
src["instructions"] = (
    "**Fill in the blanks to complete the action file.** This matches the course solution: "
    "read three slots, apply `[:100]` to `recipient` (free-text cap), compare placeholders "
    "case-insensitively, then send the demo confirmation. Copy the completed script into "
    "`level4/actions/action_process_transfer.py` and run the code assessment."
)
src["text"] = (
    "Complete the action that reads the three transfer slots (`amount`, `recipient`, `account_from`), "
    "caps `recipient` at 100 characters, re-prompts when any value is a placeholder, and otherwise sends "
    "a demo transfer confirmation:\n\n"
    "```python\nfrom typing <<<Any, Dict, List, Text>>>\n\n"
    "from rasa_sdk import Action, Tracker\nfrom rasa_sdk.executor import CollectingDispatcher\n\n\n"
    "class ActionProcessTransfer(<<<Action>>>):\n"
    '    """A custom action that processes a money transfer using multiple slots."""\n\n'
    "    def name(self) -> Text:\n        return \"<<<action_process_transfer>>>\"\n\n"
    "    def run(\n        self,\n        dispatcher: CollectingDispatcher,\n        tracker: Tracker,\n"
    "        domain: Dict[Text, Any],\n    ) -> <<<List[Dict[Text, Any]]>>>:\n"
    "        amount = <<<tracker.get_slot(\"amount\") or \"\">>>\n"
    "        recipient = <<<(tracker.get_slot(\"recipient\") or \"\")[:100]>>>\n"
    "        account_from = <<<tracker.get_slot(\"account_from\") or \"\">>>\n\n"
    '        placeholder_values = ["amount", "recipient", "account number", "user_account_number", ""]\n'
    "        if <<<amount.lower() in [p.lower() for p in placeholder_values] or recipient.lower() in [p.lower() for p in placeholder_values] or account_from.lower() in [p.lower() for p in placeholder_values]>>>:\n"
    "            dispatcher.utter_message(text=<<<\"I need the actual amount, recipient, and source account. Please provide real values.\">>>)\n"
    "            return <<<[]>>>\n\n"
    "        dispatcher.utter_message(text=<<<f\"(Demo) Transfer of ${amount} from account {account_from} to {recipient} has been processed successfully.\">>>)\n"
    "        return <<<[]>>>\n```"
)
src["distractors"] = (
    "Any, Dict, Text\nList[Dict[Any, Any]]\nActionExecutor\n"
    'tracker.get_slot("recipient") or ""\n'
    "amount in placeholder_values\nutter_ask_recipient\n{}\nreturn None"
)
src["tokens"] = {
    "blank": blanks,
    "text": parts,
    "regexPositions": [],
}
src["guidance"] = (
    "The correct answers match the Level 4 repo solution:\n\n"
    "* **Typing & class** — `Any, Dict, List, Text`, subclass `Action`, `name()` returns "
    "`action_process_transfer`, `run()` returns `List[Dict[Text, Any]]`.\n"
    "* **Slots** — `amount` and `account_from` use `tracker.get_slot(...) or \"\"`. "
    "**Recipient** uses `(tracker.get_slot(\"recipient\") or \"\")[:100]` (100-character cap; "
    "same intent as the flow `description:` in Lab 4.1).\n"
    "* **Placeholders** — One `if` with three `.lower()` comparisons against `placeholder_values`.\n"
    "* **Messages** — Re-prompt and confirmation strings as shown; both branches `return []`.\n\n"
    "Paste into `level4/actions/action_process_transfer.py` and run the **Code Test** assessment."
)

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent="\t", ensure_ascii=False)
    f.write("\n")

print("Wrote", path)
