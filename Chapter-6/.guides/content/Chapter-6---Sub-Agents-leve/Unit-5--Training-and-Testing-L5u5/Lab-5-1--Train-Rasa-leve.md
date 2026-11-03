<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Train Rasa with your new sub-agent configurd.

With all three files in place, activate the venv, export your OpenAI API key, then train from `chapter6/`.

```bash
source .venv/bin/activate 
## Add OpenAIkey back in if exported locally in the prior chapter
echo 'OPENAI_API_KEY=paste-your-key-here' >> /home/codio/workspace/.env
cd chapter6
python -m rasa train
```

The key is needed before train time because chapter 6 uses `openai-gpt-5-mini` for the sub-agent's reasoning loop and `openai-embeddings` for the enterprise search vector store. Without it, training will fail.

A model is written to `chapter6/models/`. Run the Code Test once training finishes.

{Check It!|assessment}(code-output-compare-501060004)
 