Each slot needs a matching ask response in the domain. Below are the three slots that we will add in the context of a transfer money flow. The naming convention in Rasa is `utter_ask_<slot_name>`:
 
| Slot | Ask response | Status |
|---|---|---|
| `account` | `utter_ask_account` | Already exists |
| `amount` | `utter_ask_amount` | New in Chapter 4 |
| `recipient` | `utter_ask_recipient` | New in Chapter 4 |
 
The action reads each slot by the same name with `tracker.get_slot("<slot_name>")`. A mismatch between the slot name in the domain, the flow, and the action is one of the most common problems developers encounter with slots. 
 