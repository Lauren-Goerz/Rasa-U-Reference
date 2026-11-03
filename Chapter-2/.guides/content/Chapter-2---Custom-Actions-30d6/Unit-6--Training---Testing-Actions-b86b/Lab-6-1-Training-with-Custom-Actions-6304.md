
<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Training works the same accross the course. `rasa train` reads `domain/` and `data/`, learns your action names from the `actions:` section, and writes a model to `models/`.
 
> Editing Python files does not require retraining. The action server loads code at startup. Only changes to `domain/` or `data/` files need a new training run.
 
---
 
**1. Check to make sure your .venv is active, if not run:**
 
```bash
cd /home/codio/workspace
source .venv/bin/activate
```
 
---
 
**2. Train from inside `chapter2/`**
 
```bash
cd chapter2
python -m rasa train
```
 
---
 
**3. Confirm the model was created**
 
Check that `chapter2/models/` contains a new `.tar.gz` file before running the assessment.
 
{Check It!|assessment}(code-output-compare-1070925386)
 
---