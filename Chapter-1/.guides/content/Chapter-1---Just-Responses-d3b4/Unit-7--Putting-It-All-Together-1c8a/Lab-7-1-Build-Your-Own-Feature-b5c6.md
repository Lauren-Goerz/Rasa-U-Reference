<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Add one new response and one new flow, then test.
 
1. Add a new response to `domain/basics.yml` (e.g. branch locations or an FAQ entry).
2. Create a new flow file in `data/basics/` that uses it. Write a clear `description:`.
3. Stop Inspector if running (Ctrl+C in the Inspector terminal).
4. Train:
```bash
source .venv/bin/activate
cd chapter1
python -m rasa train
```
 
5. Start Inspector and test your new flow.
```bash
python -m rasa inspect
```
 
<table style="width:100%;border-collapse:collapse;margin:16px 0;"><tr style="background:transparent;border:none;"><td style="background:#fff9ed;border:1px solid #ffd594;border-left:3px solid #f59e0b;padding:12px 16px;line-height:1.6;color:#080327;font-size:0.9em;"><strong>Always stop Inspector before training, then start a new session after.</strong> An open Inspector session uses the previous model until restarted.</td></tr></table>

{Check It!|assessment}(code-output-compare-7772000001)