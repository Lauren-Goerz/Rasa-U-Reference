<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Test how your agent can handle multiple memory items.

Make sure you have a trained model in `chapter4/models/` before starting. From `chapter4/` with the venv active:
 
```bash
python -m rasa inspect 
```
 
Click **Rasa Inspect** in the menu above this page to open Inspector.
 
Run through the steps below in order. At step 6, Rasa asks for the account number again even though you provided it in step 2. `check_balance` persisted the slot, but `ask_before_filling: true` overrides it.
 
| Step | You type | What to notice |
|---|---|---|
| 1 | `What's my balance?` | Agent asks for your account number |
| 2 | `123456` | Agent returns a balance. The `account` slot is now persisted. |
| 3 | `I'd like to transfer some money` | Agent enters the transfer flow |
| 4 | `200 dollars` | `amount` fills, agent asks for recipient |
| 5 | `Alice` | `recipient` fills, agent asks for account |
| 6 | `123456` | Rasa asks again rather than reusing the persisted value |
| 7 | *(read only)* | `action_process_transfer` fires: Transfer of $200 from account 123456 to Alice has been processed. |
 
**Try with upfront information.** Type `/restart` to reset, then try:
 
> `I'd like to transfer $50 to Alice`
 
Rasa extracts `amount` and `recipient` from that message and skips straight to asking for the account number. Only `account` is held back because `ask_before_filling: true` prevents it from filling without an explicit question. Try variations: include only the amount, only the recipient, or neither. Each time, Rasa asks only for what is still missing.