<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Train your agent to apply new search capabilities.

During training, `EnterpriseSearchPolicy` indexes the `.txt` files in `docs/` recursively. Because this course uses FAISS as the vector store, the resulting index is stored on disk locally. When the agent loads, that index is loaded into memory and used for retrieval. 

This on-disk and in-memory behaviour is specific to FAISS. If you were connecting to Milvus or Qdrant in production, indexing and retrieval would go through those external services instead.
 
Make sure `pattern_search` is overridden to call `action_trigger_search` before training, otherwise knowledge questions will not reach Enterprise Search.

## Step 1: Ensure OpenAI key is exported
 
To make Enterprise Search run, we added a new model group for OpenAI. You will need an OpenAI key for this. If you didn't add the key in chapter 1, you will need to add it now at the project root. 
 
```
echo 'OPENAI_API_KEY=your-openai-api-key' >> .env
```

## Step 2: Enter the chapter 5 folder, ensure virtual environment is active

```bash
cd chapter5
```
If your venv isn't active, run:
```bash
source .venv/bin/activate
```

## Step 3: Train Rasa

 
```bash
python -m rasa train
```
 
 {Check It!|assessment}(code-output-compare-2499735948)
