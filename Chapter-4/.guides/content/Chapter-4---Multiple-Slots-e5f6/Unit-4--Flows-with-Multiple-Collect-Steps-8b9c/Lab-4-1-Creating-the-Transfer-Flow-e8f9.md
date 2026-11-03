
<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Create `chapter4/data/basics/transfer_money.yml`: a Flow that can collect multiple slots. 
 
```yaml
flows:
  transfer_money:
    name: transfer money
    description: |
      Transfer money in USD. Steps: get dollar amount, then who receives it (any name or text), then which account to take it from, then run the transfer action.
    steps:
      - collect: amount
        description: |
          US dollar amount. Parse the user's message and set slot amount to the main number as text (e.g. 20 from "20 dollars").
      - collect: recipient
        description: |
          Transfer recipient / payee (free text).
          Extract the recipient identifier from the user's message.
          - Good examples: "Jen", "Sarah Connor", "Fred", etc.
          - If the user provides a longer sentence, extract only the recipient part (e.g. "send it to Jen please" -> "Jen").
          - If the user provides multiple recipients (e.g. "Jen or Joe"), ask again (do not guess).
      - collect: account
        ask_before_filling: true
        description: |
          A numeric account number consisting ONLY of digits (e.g., 123456, 987654321).
          CRITICAL: Do NOT extract this slot unless the user explicitly provides numbers.
          Do NOT extract from phrases like "account balance", "check account", "my account".
          Only extract when the user says actual digits like "123456" or "my account number is 789012".
      - action: action_process_transfer
```
**A note on slot descriptions** 
You will notice in the flow template above, there are some very detailed slot descriptions. These are “instructions to the language model” for how to extract a slot value, so they directly improve the reliability of slot filling, especially for ambiguous or structured values (numbers, IDs, constrained formats) and when user messages contain extra words
 
 **A note on `ask_before_filling`** 
`account` has `ask_before_filling: true` because another flow, `check_balance`, persists that slot. Without it, a returning user's account would be silently reused without confirmation. `amount` and `recipient` have no such risk, so they fill immediately if provided upfront.
 
## Verify

`data/basics/transfer_money.yml` should contain a `transfer_money` flow with three `collect:` steps and `ask_before_filling: true` on the `account` step.
 
{Check It!|assessment}(code-output-compare-401040001)
 
---