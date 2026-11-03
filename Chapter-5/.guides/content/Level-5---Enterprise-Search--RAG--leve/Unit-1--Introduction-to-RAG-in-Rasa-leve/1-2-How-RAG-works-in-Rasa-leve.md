RAG runs two steps for every knowledge question: retrieve relevant content, then generate an answer guided by what was retrieved.
 
<div style="display:flex; flex-direction:column; gap:12px; margin:24px 0; font-family:'IBM Plex Sans',sans-serif; font-size:14px;">
  <div style="display:flex; gap:16px; align-items:flex-start; border:1px solid #dfe8ff; border-radius:6px; padding:16px; background:#fff;">
    <div style="flex-shrink:0; width:32px; height:32px; border-radius:50%; background:#5a17ee; color:#fff; font-weight:700; font-size:14px; display:flex; align-items:center; justify-content:center;">1</div>
    <div>
      <div style="font-weight:600; font-size:15px; margin-bottom:6px; color:#080327;">Embed and retrieve</div>
      <div style="color:#444; line-height:1.6;">An embedding model converts text into a vector — a list of numbers that captures meaning. Chunks with similar meaning end up with similar vectors, even if they use different words. At train time, Rasa indexes the <code>.txt</code> files under <code>docs/</code>, creates embeddings, and stores the index on disk. At runtime, the index loads into memory and <a href="https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/">FAISS</a> searches it for the most relevant chunks. For production workloads, Rasa recommends Milvus or Qdrant instead of FAISS.</div>
    </div>
  </div>
  <div style="display:flex; gap:16px; align-items:flex-start; border:1px solid #dfe8ff; border-radius:6px; padding:16px; background:#fff;">
    <div style="flex-shrink:0; width:32px; height:32px; border-radius:50%; background:#5a17ee; color:#fff; font-weight:700; font-size:14px; display:flex; align-items:center; justify-content:center;">2</div>
    <div>
      <div style="font-weight:600; font-size:15px; margin-bottom:6px; color:#080327;">Generate an answer</div>
      <div style="color:#444; line-height:1.6;">The retrieved chunks are passed to the LLM as context. The LLM writes an answer grounded in what was retrieved. This is <strong>generative search</strong>, the default mode. Rasa also supports <strong>extractive search</strong>, which returns the closest pre-written answer verbatim with no LLM generation.</div>
    </div>
  </div>
</div>
<div style="border-left:3px solid #5a17ee; padding:12px 16px; background:#f7f7f7; border-radius:0 6px 6px 0; margin:24px 0; font-family:'IBM Plex Sans',sans-serif; font-size:14px; color:#444; line-height:1.6;">
  <div style="font-weight:600; color:#080327; margin-bottom:6px;">How knowledge questions reach Enterprise Search</div>
  <code>SearchReadyLLMCommandGenerator</code> emits a <code>KnowledgeAnswerCommand</code>, which triggers <code>pattern_search</code>. By default, <code>pattern_search</code> responds with <code>utter_no_knowledge_base</code>. To wire in Enterprise Search, override <code>pattern_search</code> to call <code>action_trigger_search</code>, a default action added by <code>EnterpriseSearchPolicy</code> that runs retrieval and generation. Lab 5.3.1 covers this override.
</div>
