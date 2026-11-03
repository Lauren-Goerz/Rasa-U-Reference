`config.yml` defines how Rasa builds and processes your agent.
 
```yaml
recipe: default.v1
language: en
assistant_id: chapter1-agent
 
pipeline:
  - name: SearchReadyLLMCommandGenerator
    llm:
      model_group: rasa_command_generation_model
    flow_retrieval:
      active: false
 
policies:
  - name: FlowPolicy
```
 
| Field | What it does |
|---|---|
| `recipe` | Base configuration template. `default.v1` is standard. |
| `language` | Agent language. `en`, `fr`, etc. |
| `assistant_id` | Unique name visible in logs, useful when comparing model versions. |
| `pipeline` | Defines how Rasa processes user messages. `SearchReadyLLMCommandGenerator` reads flow `description:` fields to select a flow. |
| `model_group` | References the LLM configuration in `endpoints.yml`. Keeps model definitions separate from pipeline config. |
| `flow_retrieval` | Pre-selects flows relevant to the current message before sending to the LLM. Set to `false` here because this project has few flows. |
| `policies` | Defines what the agent does next. `FlowPolicy` manages flow-based conversations. |
 
{Check It!|assessment}(multiple-choice-2496482437)
 
---