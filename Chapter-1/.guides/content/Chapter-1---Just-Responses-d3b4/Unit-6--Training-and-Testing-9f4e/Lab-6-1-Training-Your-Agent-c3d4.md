 
<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>
Run all commands from `chapter1/` with the virtual environment active.
 
```bash
source .venv/bin/activate
cd chapter1
python -m rasa --version
python -m rasa train
```
 
Your prompt should show `(.venv)` and `pwd` should end with `chapter1`.
 
If `python -m rasa --version` fails:
 
```bash
pip install rasa-pro==3.17.0
echo 'RASA_LICENSE=YOUR_LICENSE_KEY' > .env
```
 
Installing Rasa takes several minutes. On success:
 
```text
INFO  rasa.model - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'
```
 
**Common errors**
If you have a problem not solved by this chart, paste your logs into the rasa docs bot on https://rasa.com/docs/ and it might be able to find the root cause. 
 
| Symptom | Fix |
|---|---|
| YAML or parse error with a file path and line | Open the file at that line. Use 2 spaces, not tabs. Check colons after keys and `-` before list items. Make sure you are training again from `chapter1/` and not the root. |
| "block mapping" YAML syntax error | Fix indentation and structure, save, train again from `chapter1/`. |
| `utter_…` response not found | A flow references a response missing from `domain/basics.yml`. Add the response or fix the name. |
| No module named `rasa` | Activate the venv from the project root, `cd chapter1`, then `pip install rasa-pro==3.17.0`. |
| `RASA_LICENSE` not set | See Lab 0.1, or ask your instructor. |
 
<table style="width:100%;border-collapse:collapse;margin:16px 0;"><tr style="background:transparent;border:none;"><td style="background:#fff9ed;border:1px solid #ffd594;border-left:3px solid #f59e0b;padding:12px 16px;line-height:1.6;color:#080327;font-size:0.9em;">Confirm <code>chapter1/models/</code> contains a new <code>.tar.gz</code> before clicking Check It!. The assessment expects a model trained within the last 10 minutes, if you trained earlier, run <code>python -m rasa train</code> again.</td></tr></table>

{Check It!|assessment}(code-output-compare-2562507355)
 
---
 