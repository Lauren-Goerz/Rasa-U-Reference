<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Test your agent's search capabilities.

### Inspector
From `chapter5/` with the venv active:
```bash
python -m rasa inspect
```
Open up "Rasa Inspect" from the menu bar above this page.
 
Ask `What is the fee for an international wire transfer?`. The answer should come from `banking_policies.txt`.
 
Try some other questions your docs can answer but that no flow covers:
- `What is the daily transfer limit for a standard account?`
- `How much does an international wire transfer cost?`
- `What APY does the savings account earn?`
- `Do you charge ATM fees?`

Each should return a specific answer from the documents. If the agent says it has no knowledge base, the `pattern_search` override is missing.
 
**Mid-flow test:** Start a transfer, then ask `what is the transfer fee?`. The agent should answer from the docs and return to the transfer.  
Also check that the rest of the agent works as before. Every flow and policy in chapter 5 is accounted for below.
 
| Flow or policy | Trigger | Response source |
|----------------|---------|-----------------|
| `greet`, `help`, `contact`, `goodbye` | Named intent phrases | `domain/*.yml` responses |
| `hours`, `holiday_hours` | Bank hours queries | Custom actions |
| `check_balance` | Balance queries | `action_check_balance_simple` |
| `transfer_money` | Transfer requests | `action_process_transfer` |
| `pattern_search` | Knowledge questions | `EnterpriseSearchPolicy` + `docs/` |
 
To update the knowledge base, edit the `.txt` files in `docs/` and retrain.