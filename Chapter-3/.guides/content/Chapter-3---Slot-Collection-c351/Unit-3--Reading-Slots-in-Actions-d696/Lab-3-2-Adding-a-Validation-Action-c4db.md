A ValidationAction` is a special action class that runs automatically after a slot is collected. You do not call it from a flow. Rasa calls it. When it returns `{"account": None}`, Rasa treats the slot as empty and re-collects it using `utter_ask_account`. When it returns a value, the flow continues.
 
This is different from a regular `Action`, which you call explicitly with `action: action_name`. The `ValidationAction` runs behind the scenes on every slot collection in the conversation.
 
## The action
 
Create `level3/actions/validate_account_slot.py`:
 
```python
from typing import Any, Dict, Text
 
from rasa_sdk import Tracker, ValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
 
 
class ValidateAccountSlot(ValidationAction):
    """Validates the account slot to reject placeholder values."""
 
    def validate_account(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
 
        placeholder_values = ["account number", "user_account_number", "<missing>"]
 
        if slot_value and slot_value.lower() in [p.lower() for p in placeholder_values]:
            return {"account": None}
 
        return {"account": slot_value}
```
 
Two things to note:
 
- **No `name()` method.** Do not add one. `ValidationAction` has a fixed name hardcoded as `action_validate_slot_mappings`. If you override it, the validation will not run.
- **Method naming.** The method `validate_account` maps to the slot `account`. For any other slot, the method name is `validate_<slot_name>`.
## Register in the domain
 
Add `action_validate_slot_mappings` to the `actions:` list in `domain/basics.yml`. This is the fixed name Rasa uses internally — you do not define it yourself, only register it:
 
```yaml
actions:
  - action_bank_hours
  - action_holiday_hours
  - action_check_balance
  - action_validate_slot_mappings
```
 
## How the two actions work together
 
When the flow reaches `collect: account`:
 
1. Rasa sends `utter_ask_account` and waits for a value.
2. `action_validate_slot_mappings` runs automatically and calls `validate_account`.
3. If the value is a placeholder, `validate_account` returns `{"account": None}`. Rasa re-asks.
4. If the value passes, the slot is set and the flow continues to `action_check_balance`.
5. `action_check_balance` reads the slot. No placeholder check needed.
## Verify
 
- `actions/validate_account_slot.py` exists with the class `ValidateAccountSlot` and a `validate_account` method
- No `name()` method is defined on the class
- `action_validate_slot_mappings` is listed under `actions:` in `domain/basics.yml`

