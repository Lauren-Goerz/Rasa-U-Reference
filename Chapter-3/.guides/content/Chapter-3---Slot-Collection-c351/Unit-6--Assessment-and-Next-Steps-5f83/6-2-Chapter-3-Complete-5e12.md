<table style="width:100%;border-collapse:collapse;margin:0 0 32px;">
  <tr style="background:transparent;border:none;">
    <td style="background:#ebe8fe;border:1px solid #c4baf9;padding:40px 32px;text-align:center;border-radius:6px;">
      <img src=".guides/img/L3_memory.gif" alt="Chapter 3 complete" style="max-width:160px;margin:0 auto 24px;display:block;border-radius:4px;">
      <p style="font-size:1.6em;font-weight:700;color:#080327;margin:0 0 8px;letter-spacing:-.02em;">Chapter 3 complete.</p>
      <p style="font-size:0.9em;color:#636C85;margin:0;">Your agent can now store and recall memory items (slots) across turns.</p>
    </td>
  </tr>
</table>
What you covered:
 
- Slots are named memory variables defined in the domain and set during a conversation
- A `collect:` step sends `utter_ask_<slot_name>`, waits for a reply, and stores the extracted value
- The `description` field guides the LLM on what a valid value looks like at the point of extraction
- A `rejections` block validates the extracted value and re-prompts when the condition fails
- `persisted_slots` carries values forward into the next session, skipping the collect step when the value is already set

**Next:** Chapter 4 adds multi-slot collection: a transfer flow that collects an account number, a target account, and an amount in a single conversation.

<p style="margin:32px 0 0;padding:12px 16px;background:#EFF1FF;border-left:3px solid #5a17ee;font-size:0.85em;color:#080327;">Click <strong>Mark as complete</strong> in the top righthand side of this page before moving on to the next section. Required to start the next chapter. </p>
 
<hr>
<table style="width:100%;border-collapse:collapse;margin-top:20px;">
<tr style="background:transparent;border:none;">
<td style="padding:0 16px 0 0;vertical-align:middle;border:none;background:transparent;">
<p style="font-size:0.80em;color:#636C85;margin:0;line-height:1.6;">Think Rasa might be a good fit for your team? Get in touch. Stuck on setup? The Rasa community is happy to help.</p>
</td>
<td style="padding:0;vertical-align:middle;text-align:right;border:none;background:transparent;white-space:nowrap;">
<a href="https://hellorasa.info/4ww4pyj" target="_blank" style="display:inline-block;font-size:0.78em;font-weight:500;color:#5a17ee;background:transparent;padding:6px 12px;border-radius:2px;text-decoration:none;border:1px solid #5a17ee;margin-right:8px;">Connect with Rasa</a><a href="https://hellorasa.info/4fdv6RV" target="_blank" style="display:inline-block;font-size:0.78em;font-weight:500;color:#5a17ee;background:transparent;padding:6px 12px;border-radius:2px;text-decoration:none;border:1px solid #5a17ee;">Join Discord</a>
</td>
</tr>
</table>
