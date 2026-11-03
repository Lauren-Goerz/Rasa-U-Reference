In Rasa, flows are built from different step types: `collect`, `action`, `set_slots`, `call`, `link`, and others. The step type determines what happens: collecting a slot, running logic, or sending a reply.
 
This chapter focuses on the `action` step type, which has three variants:
 
| Type | Source | Logic |
|---|---|---|
| **Response** `utter_*` | Text you wrote in YAML | None, static only |
| **Custom action** `action_*` | Python class you write | Anything: API calls, calculations, database queries |
| **Default action** | Built into Rasa | Fixed, manages conversation state automatically |
 
Use a response when the text never changes. Use a custom action when the reply depends on something evaluated at runtime, the current date, a database value, an API response.
 
**Bank hours example**
 
A response locks you into fixed text:
 
```yaml
utter_hours:
  - text: "We're open Monday-Friday 9am-5pm, Saturday 10am-2pm."
```
 
A custom action checks what day it actually is:
 
```python
def run(self, dispatcher, tracker, domain):
    weekday = datetime.now().weekday()
    if weekday == 6:
        dispatcher.utter_message(text="Today is Sunday, we're closed.")
    elif weekday == 5:
        dispatcher.utter_message(text="Today is Saturday, open 10am-2pm.")
    else:
        dispatcher.utter_message(text="We're open today until 5pm.")
    return []
```
 
Custom actions run in a separate process called the **action server**. When a flow reaches an `action` step, the Rasa Framework sends an HTTP request to it, the action server executes your `run()` method, and returns the reply.
 
<table style="width:100%;border-collapse:collapse;margin:20px 0 8px;">
<tr style="background:transparent;border:none;">
<td style="width:42%;background:#f0f1ff;border:1px solid #dfe8ff;border-radius:6px;padding:20px 22px;vertical-align:top;">
<p style="font-size:10px;color:#a882f5;margin:0 0 8px;letter-spacing:.1em;text-transform:uppercase;">Rasa Framework</p>
<p style="font-size:0.85em;color:#444;margin:0;line-height:1.6;">Manages dialogue and conversation state. Sends an HTTP request to the action server when a flow step calls a custom action.</p>
</td>
<td style="width:16%;text-align:center;vertical-align:middle;border:none;background:transparent;padding:0 8px;">
<p style="margin:0;font-size:0.75em;color:#aaa;line-height:1.8;">HTTP<br>⇄</p>
</td>
<td style="width:42%;background:#fafafa;border:1px solid #e8eaf0;border-radius:6px;padding:20px 22px;vertical-align:top;">
<p style="font-size:10px;color:#bbb;margin:0 0 8px;letter-spacing:.1em;text-transform:uppercase;">Action Server</p>
<p style="font-size:0.85em;color:#636C85;margin:0;line-height:1.6;">A separate process that runs your Python. Receives the request, executes <span style="font-family:monospace;font-size:0.95em;">run()</span>, and returns the reply.</p>
</td>
</tr>
</table>

> Editing Python files does not require retraining. The action server loads code at startup. Only changes to `domain/` or `data/` require a new training run.
 
---