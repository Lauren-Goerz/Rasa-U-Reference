<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Train your agent with multiple slots.

From your workspace root:
 
```bash
# Check to make sure .venv is active. If .venv is missing: python3.11 -m venv .venv && source .venv/bin/activate
source .venv/bin/activate

cd chapter4
python -m rasa train
```
 Training takes about a minute. A successful run produces output like:
 
```text
INFO  rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'
```
 
**Verify.** `chapter4/models/` contains a new `.tar.gz` file.
 
{Check It!|assessment}(code-output-compare-401050001)
 
---
