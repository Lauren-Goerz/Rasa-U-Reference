In Chapter 5, you gave the banking agent knowledge. By adding `.txt` files to `docs/`, the agent could answer questions like "What is the ATM fee?" or "What is the daily transfer limit?" without you writing a flow for every possible question. Rasa indexed the documents at train time; at runtime, the `EnterpriseSearchPolicy` retrieved the relevant content and used `openai-gpt-5-mini` to generate an answer.
 
That works because the question has a lookup shape. User asks. Agent retrieves. Agent answers.
 
Now consider: "I'm thinking about taking out a loan. What makes sense for me?" There is no document that answers that. The right response is a conversation: find out what the user is trying to achieve, look up relevant products, run a repayment calculation, and adapt to what the user says next. No fixed steps. No pre-defined sequence.
 
That is what a sub-agent is for.
 
Chapter 6 introduces two new things: **MCP** and **sub-agents**.
 
**MCP** (Model Context Protocol) is an open standard for making callable functions, called **tools**, available to an LLM. Instead of a Rasa custom action running inside the action server, an MCP server exposes functions the LLM can call directly during its reasoning loop.
 
A **sub-agent** is a separate Rasa agent that connects to an MCP server, uses its tools to complete a task, and hands control back to the main agent when it is done. The main agent delegates to it with a single `call:` step in a flow.
 
<div style="margin: 32px 0;">
<style>
  .build-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
  .build-card {
    background: #fff;
    border: 1px solid #dfe8ff;
    border-top: 3px solid #5a17ee;
    border-radius: 8px;
    padding: 18px;
  }
  .build-lab { color: #5a17ee; font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase; font-weight: 600; margin-bottom: 10px; font-family: 'IBM Plex Sans', sans-serif; }
  .build-file { color: #080327; font-size: 13px; font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; margin-bottom: 10px; line-height: 1.4; }
  .build-desc { color: #636C85; font-size: 12px; line-height: 1.6; margin: 0; font-family: 'IBM Plex Sans', sans-serif; }
  @media (max-width: 700px) { .build-grid { grid-template-columns: 1fr; } }
</style>
<div class="build-grid">
  <div class="build-card">
    <div class="build-lab">New in Chapter 6</div>
    <div class="build-file">MCP</div>
    <p class="build-desc">An open standard for exposing callable functions to an LLM. The <code>banking_mcp</code> server provides the financial advisor's tools.</p>
  </div>
  <div class="build-card">
    <div class="build-lab">New in Chapter 6</div>
    <div class="build-file">Sub-agent</div>
    <p class="build-desc">A separate Rasa agent with its own LLM. Runs a ReAct reasoning loop, calls MCP tools, and signals completion with <code>task_completed</code>.</p>
  </div>
  <div class="build-card">
    <div class="build-lab">New in Chapter 6</div>
    <div class="build-file">Flow orchestration</div>
    <p class="build-desc">The main agent delegates to the sub-agent via <code>call: financial_advisor</code> in a flow. Control returns when the sub-agent is done.</p>
  </div>
</div>
</div>


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
