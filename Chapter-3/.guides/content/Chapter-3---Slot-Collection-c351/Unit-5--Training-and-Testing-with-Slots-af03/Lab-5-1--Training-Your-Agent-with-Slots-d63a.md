<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>
Complete Labs 2.1 through 4.1 before running this step. Training will fail if any slot, response, or action name is missing or mismatched.
 
From your workspace root:
 
```bash
# check that your .venv is active, if not:
source .venv/bin/activate
# If .venv is missing: python3.11 -m venv .venv && source .venv/bin/activate
 
cd chapter3
python -m rasa train
```
 
 Training takes about a minute. A successful run produces output like:
 
```text
INFO  rasa.model  - Successfully saved model to 'models/20250112-120817-descent-lard.tar.gz'
```
 
**Verify.** `chapter3/models/` contains a new `.tar.gz` file.
 
{Check It!|assessment}(code-output-compare-1029038275)
 
---