Every slot follows three steps.
 
<table style="width:100%;border-collapse:collapse;margin:24px 0;font-family:'IBM Plex Sans',system-ui,sans-serif;">
  <tr>
    <td style="width:33%;padding:14px 18px;background:#EFF1FF;border-right:3px solid #fff;vertical-align:top;">
      <div style="font-size:11px;font-weight:700;color:#5a17ee;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:4px;">1 &mdash; Define</div>
      <div style="font-size:12px;color:#3d3d5c;font-family:monospace;">domain/*.yml</div>
    </td>
    <td style="width:33%;padding:14px 18px;background:#DADCFB;border-right:3px solid #fff;vertical-align:top;">
      <div style="font-size:11px;font-weight:700;color:#5a17ee;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:4px;">2 &mdash; Set</div>
      <div style="font-size:12px;color:#3d3d5c;font-family:monospace;">data/flows/*.yml</div>
    </td>
    <td style="width:33%;padding:14px 18px;background:#EFF1FF;vertical-align:top;">
      <div style="font-size:11px;font-weight:700;color:#5a17ee;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:4px;">3 &mdash; Read</div>
      <div style="font-size:12px;color:#3d3d5c;font-family:monospace;">actions/*.py</div>
    </td>
  </tr>
</table>

**Define** the slot in `domain/basics.yml`:
 
```yaml
slots:
  account:
    type: text
```
 
**Set** it in a flow using `collect:`. When the flow reaches this step, Rasa sends `utter_ask_account`, waits for a reply, and stores the extracted value. If the slot already has a value, the step is skipped.
 
```yaml
steps:
  - collect: account
  - action: action_check_balance_simple
```
 
Slots can also be set directly in a flow with `set_slots:`, or via a `SlotSet` event returned from an action. Chapter 3 uses the `collect` path.
 
**Read** it in a custom action via the tracker:
 
```python
account = tracker.get_slot("account")
```
 
The labs follow this order: domain first, action second, flow last.
 
---