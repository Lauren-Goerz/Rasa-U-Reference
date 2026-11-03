<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>


Add a second variation to `utter_goodbye`.
 
Find `utter_goodbye` in `domain/basics.yml` and add a second `- text:` line at the same indentation:
 
```yaml
utter_goodbye:
  - text: "Goodbye! Have a great day!"
  - text: "See you later! Take care!"
    metadata:
      rephrase: True
```
 
Be sure to save your changes.

Each time the flow calls `utter_goodbye`, Rasa picks one `text` entry at random. Adding `rephrase: True` to an entry stacks LLM rephrasing on top of that random pick.


{Check It!|assessment}(code-output-compare-302300002)

---
