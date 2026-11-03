Chapter 3 built an agent that collects one value and passes it to an action. Chapter 4 extends that pattern to flows that collect several values before running an action.
 
You will build a money transfer flow that needs three pieces of information: the account number, the amount, and the recipient. The `account` slot already exists from Chapter 3. You add `amount` and `recipient`. If the user already checked their balance in the same session, the transfer flow skips asking for the account number because the slot is already set.
 
| File | What changes |
|---|---|
| `domain/basics.yml` | Two new slots, two new ask responses, one new action name |
| `actions/action_process_transfer.py` | Action that reads all three slots |
| `data/basics/transfer_money.yml` | Flow with three collect steps |
| `models/` | Trained model |
| Inspector | End-to-end transfer test |
  


<hr>
<table style="width:100%;border-collapse:collapse;margin-top:20px;">
  <tr style="background:transparent;border:none;">
    <td style="padding:0 16px 0 0;vertical-align:middle;border:none;background:transparent;">
      <p style="font-size:0.80em;color:#636C85;margin:0;line-height:1.6;">Need help during this chapter? Your Rasa instructors are happy to help in the #rasa-university discord.</p>
    </td>
    <td style="padding:0;vertical-align:middle;text-align:right;border:none;background:transparent;white-space:nowrap;">
      <a href="https://hellorasa.info/4fdv6RV" target="_blank" style="display:inline-block;font-size:0.82em;font-weight:600;color:#ffffff;background:#5a17ee;padding:8px 18px;border-radius:2px;text-decoration:none;text-shadow:none;background-image:none;">Join Discord</a>
    </td>
  </tr>
</table>
