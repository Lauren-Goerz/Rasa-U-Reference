`endpoints.yml` defines where Rasa finds actions and how LLM features are configured.
 
```yaml
action_endpoint:
  actions_module: "actions"
 
nlg:
  type: rephrase
  llm:
    model_group: rasa_command_generation_model
 
model_groups:
  - id: rasa_command_generation_model
    models:
      - provider: rasa
        model: rasa/command-generator-llama-3.1-8b-instruct
        api_base: "https://tutorial-llm.rasa.ai"
```
 
| Field | What it does |
|---|---|
| `action_endpoint` | Points Rasa to the `actions/` folder for custom actions. Not used in Chapter 1. |
| `nlg` | Enables response rephrasing. `type: rephrase` tells Rasa to use an LLM to rewrite templated responses before sending. |
| `model_groups` | Declares the LLM provider and model. The `id` here matches `model_group` in `config.yml`. |
| `provider: rasa` | Uses the course tutorial model at `tutorial-llm.rasa.ai`. |
| `model` | A small, fine-tuned Llama 3.1 8B model optimized for this course. Not the most powerful model, but no external API key required. |
 
{Check It!|assessment}(multiple-choice-2982013912)