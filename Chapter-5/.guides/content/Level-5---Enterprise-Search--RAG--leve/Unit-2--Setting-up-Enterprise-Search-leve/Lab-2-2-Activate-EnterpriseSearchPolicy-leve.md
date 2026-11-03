 <p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Setup config.yml and endpoints.yml for enterprise search. 

In order to use the documents that you have just added, you will need to update your configuration to activate the enterprise search policy, and use a model that can support this activity. Until now, we've been using a small fine-tuned model hosted by Rasa, but for enterprise search, a stronger model is required.
 
With Rasa, you can select which models are used for specific tasks. We will keep the Rasa model for command generation for now, and use another model for enterprise search.
 
### Part A: config.yml
In `chapter5/config.yml`, add `EnterpriseSearchPolicy` after `FlowPolicy` under `policies:`.
```yaml
policies:
  - name: FlowPolicy
  - name: EnterpriseSearchPolicy
    vector_store:
      type: faiss
      source: ./docs
    llm:
      model_group: openai-gpt-5-mini
    embeddings:
      model_group: openai-embeddings
    check_relevancy: true
 ```

 
### Part B: endpoints.yml
 
Enterprise Search needs two things the command generator does not provide: a general-purpose LLM to write answers from retrieved chunks, and an embeddings model to index the documents. Both use OpenAI, so one API key covers everything.
 
Add both model groups to `chapter5/endpoints.yml`, keeping the existing `rasa_command_generation_model` group.
 
```yaml
model_groups:
  - id: rasa_command_generation_model
    models:
      - provider: rasa
        model: rasa/command-generator-llama-3.1-8b-instruct
        api_base: "https://tutorial-llm.rasa.ai"
 
  - id: openai-gpt-5-mini
    models:
      - provider: openai
        model: gpt-5-mini-2025-08-07
        reasoning_effort: "minimal"
        timeout: 15
 
  - id: openai-embeddings
    models:
      - provider: openai
        model: text-embedding-3-large
        
```
 
Leave `action_endpoint`, `nlg`, and everything else unchanged. We will export your OpenAI key to use this newly added model just before training when we open the terminal. 
 
  


{Check It!|assessment}(code-output-compare-2989029150)

