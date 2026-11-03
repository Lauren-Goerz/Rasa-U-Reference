**Inspector** is Rasa's built-in testing UI. In Codio, use the **Rasa Inspect** tab in the top menu. On your own machine, open a browser to `localhost`.
 
**1. Confirm setup**
 
Stay in `chapter1/` with the venv active (`(.venv)` in your prompt). If not:
 
```bash
source .venv/bin/activate
cd chapter1
```
 
**2. Create the logs folder**
 
```bash
mkdir -p logs
```
 
**3. Start Inspector**
 
```bash
python -m rasa inspect --debug --log-file logs/logs.out
```
 
Wait for:
 
```text
INFO     sanic.server  - Starting worker [400]
```
 
<table style="width:100%;border-collapse:collapse;margin:16px 0;"><tr style="background:transparent;border:none;"><td style="background:#fff9ed;border:1px solid #ffd594;border-left:3px solid #f59e0b;padding:12px 16px;line-height:1.6;color:#080327;font-size:0.9em;"><strong>Leave this terminal open.</strong> Inspector is a server process. Closing the terminal stops Inspector.</td></tr></table>


##### How to navigate Inspector once it's running: 

<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;max-width:100%;">
  <iframe src="https://www.youtube.com/embed/0ZSvH5OFy-E" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allowfullscreen></iframe>
</div>


**4. Open the chat**
 
Click the **Rasa Inspect** tab in the top menu. Type `hello` and press Enter. The agent should reply.
 
Try a few more messages:
- "How do I contact support?"
- "What can you do?"
- "Hi!"
{Check It!|assessment}(code-output-compare-2562507356)
 
**Inspector panels**
 
| Panel | Use it for |
|---|---|
| **Chat** | Type messages and read replies. Scroll back to review. |
| **Flow / diagram** | See which flow activated for the last turn. Wrong flow? Improve the `description:` on that flow. |
| **Debug** | Lists what was triggered and metadata. Ignore at first; useful when behavior is wrong. The tracker outlines every decision Rasa made |
| **Slots** | Shows remembered values. Empty in Chapter 1 — slots are introduced in Chapter 3. |
 
---

---


