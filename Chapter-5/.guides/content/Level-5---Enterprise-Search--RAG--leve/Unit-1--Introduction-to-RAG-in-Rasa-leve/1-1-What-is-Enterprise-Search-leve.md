This chapter adds enterprise search to your banking agent using retrieval-augmented generation (RAG).
 
With RAG, the agent:
 
1\. Searches documents for relevant information  
2\. Uses an LLM to generate an answer based on what it finds
 
When you use RAG, you can delegate FAQ questions like "What is the fee for international transfers?" using your existing documents instead of hard coding every response.
 
In Rasa, this is done with the `EnterpriseSearchPolicy`. You store knowledge in .txt files, Rasa indexes them during training, and at runtime the agent retrieves content and generates an answer, no new flows or responses needed. 


<hr>
<table style="width:100%;border-collapse:collapse;margin-top:20px;">
  <tr style="background:transparent;border:none;">
    <td style="padding:0 16px 0 0;vertical-align:middle;border:none;background:transparent;">
      <p style="font-size:0.80em;color:#636C85;margin:0;line-height:1.6;">Need help during this chapter? Your Rasa instructors are happy to help in the #rasa-university discord.</p>
    </td>
    <td style="padding:0;vertical-align:middle;text-align:right;border:none;background:transparent;white-space:nowrap;">
      <a href="https://hellorasa.info/4fdv6RV" target="_blank" style="display:inline-block;font-size:0.82em;font-weight:600;color:#ffffff;background:#5a17ee;padding:8px 18px;border-radius:2px;text-decoration:none;text-shadow:none;background-image:none;">Join Discord</a>
    </td>
  </tr>
</table>