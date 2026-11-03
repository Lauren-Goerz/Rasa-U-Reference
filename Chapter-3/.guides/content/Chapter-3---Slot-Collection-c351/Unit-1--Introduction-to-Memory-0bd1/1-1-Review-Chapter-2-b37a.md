Your Chapter 2 agent can run custom Python and look things up. It cannot remember anything between turns.

> **User:** Check my balance.
> **Agent:** What is your account number?
> **User:** 1234
> **Agent:** What account number?

The agent had no place to store the value. In Chapter 3, you’ll learn how to capture information from the conversation and make it available to later steps, later turns, and other flows.

> **User:** Check my balance.
> **Agent:** What is your account number?
> **User:** 1234
> **Agent:** The balance for account 1234 is $123.45.

Later in the same session:

> **User:** Can I transfer some money?
> **Agent:** How much would you like to transfer from account 1234?

By the end of this chapter, your agent will ask for an account number, store it, and pass it to an action that returns a balance. You are adding your first slot, a new action, and one flow on top of everything from Chapter 2.


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
