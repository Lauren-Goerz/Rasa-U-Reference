
Rasa gives you different ways to manage dialogue depending on the shape of the conversation.
 
**Flows** handle conversations with a fixed path: collect the amount, confirm the account, process the transaction. You define every step. Reliable, auditable, easy to test.
 
**Enterprise Search** handles information questions: "What are the fees for an international transfer?" The answer lives in a document. The agent retrieves and responds. That is what Chapter 5 added.
 
**Sub-agents** handle open-ended conversations where the path cannot be defined in advance. A user exploring loan options might ask three questions you could not anticipate. There is no script that covers every branch — the right approach is an agent that reasons freely, calls functions, and adapts to wherever the conversation goes.
 
### What a sub-agent is
 
A sub-agent is a separate Rasa agent with its own LLM and its own tools. The main agent delegates to it at a specific point in a flow, then waits. The sub-agent reasons, calls functions, and decides what to do next. When it is done, it signals completion and control returns to the main flow.
 
In a flow, you write every step. With a sub-agent, you define the task scope and the available tools — the sub-agent works out the steps itself.
 
### Tools and MCP
 
The functions a sub-agent can call are called **tools**, exposed by an **MCP server**. MCP (Model Context Protocol) is an open standard for making functions available to an LLM — how it discovers tools, calls them, and receives results.
 
In this chapter, `mcp_server/banking.py` exposes three advisory tools: `get_account_options`, `get_current_rates`, and `calculate_loan_repayment`. None move money or update accounts. Regulated steps stay in the main agent's guided flows where every action is auditable.
 
 
### How to Orchestrate Sub-Agents
 
The main agent delegates to a sub-agent with a `call:` step in a flow. When that step is reached, the sub-agent takes over. It runs an agent loop: the LLM reasons about which tool to call, the tool runs via MCP, the LLM processes the result, and the loop repeats. When the sub-agent calls the built-in `task_completed` tool, the loop exits and control returns to the main flow.
 
<div style="background:#EFF1FF; border-radius:12px; padding:32px 24px; border:1px solid #dfe8ff; margin:32px 0; display:flex; flex-direction:column; align-items:center;">
  <div style="background:#fff; border:1px solid #5a17ee; border-radius:8px; padding:12px 20px; text-align:center; font-family:'IBM Plex Sans',sans-serif; font-size:13px; font-weight:500; color:#080327; width:100%; max-width:280px; box-sizing:border-box;">Main agent</div>
  <div style="color:#A6AAF3; font-size:20px; line-height:1; padding:4px 0;">↓</div>
  <div style="background:#fff; border:1px solid #dfe8ff; border-radius:8px; padding:12px 20px; text-align:center; font-family:'IBM Plex Sans',sans-serif; font-size:13px; font-weight:500; color:#636C85; width:100%; max-width:280px; box-sizing:border-box;">book_appointment.yml flow starts</div>
  <div style="color:#A6AAF3; font-size:20px; line-height:1; padding:4px 0;">↓</div>
  <div style="background:#EFF1FF; border:1px solid #5a17ee; border-radius:8px; padding:12px 20px; text-align:center; font-family:'IBM Plex Mono',monospace; font-size:12px; font-weight:500; color:#5a17ee; width:100%; max-width:280px; box-sizing:border-box;">call: branch_appointment_booking</div>
  <div style="color:#5a17ee; font-size:11px; letter-spacing:0.08em; text-transform:uppercase; font-weight:600; font-family:'IBM Plex Sans',sans-serif; padding:6px 0;">hand-off</div>
  <div style="color:#A6AAF3; font-size:20px; line-height:1; padding:4px 0;">↓</div>
  <div style="background:#DADCFB; border:1px solid #7e7af4; border-radius:8px; padding:12px 20px; text-align:center; font-family:'IBM Plex Sans',sans-serif; font-size:13px; font-weight:500; color:#080327; width:100%; max-width:280px; box-sizing:border-box; margin-bottom:8px;">BookAppointment sub-agent</div>
  <div style="border:1px dashed #7e7af4; border-radius:10px; padding:16px 20px; margin:8px 0; text-align:center; width:100%; max-width:300px; box-sizing:border-box; background:#fff;">
    <div style="color:#5a17ee; font-size:11px; font-weight:600; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:10px; font-family:'IBM Plex Sans',sans-serif;">Agent loop</div>
    <div style="color:#636C85; font-size:12px; font-family:'IBM Plex Mono',monospace; padding:4px 0;">LLM chooses a tool</div>
    <div style="color:#A6AAF3; font-size:14px; line-height:1;">↓</div>
    <div style="color:#636C85; font-size:12px; font-family:'IBM Plex Mono',monospace; padding:4px 0;">MCP tool runs</div>
    <div style="color:#A6AAF3; font-size:14px; line-height:1;">↓</div>
    <div style="color:#636C85; font-size:12px; font-family:'IBM Plex Mono',monospace; padding:4px 0;">LLM processes result</div>
    <div style="color:#A6AAF3; font-size:13px; padding:4px 0;">↻ repeats until done</div>
  </div>
  <div style="color:#A6AAF3; font-size:20px; line-height:1; padding:4px 0;">↓</div>
  <div style="background:#EFF1FF; border:1px solid #7e7af4; border-radius:8px; padding:12px 20px; text-align:center; font-family:'IBM Plex Mono',monospace; font-size:12px; font-weight:500; color:#5a17ee; width:100%; max-width:280px; box-sizing:border-box;">task_completed</div>
  <div style="color:#5a17ee; font-size:11px; letter-spacing:0.08em; text-transform:uppercase; font-weight:600; font-family:'IBM Plex Sans',sans-serif; padding:6px 0;">control returns</div>
  <div style="color:#A6AAF3; font-size:20px; line-height:1; padding:4px 0;">↓</div>
  <div style="background:#fff; border:1px solid #5a17ee; border-radius:8px; padding:12px 20px; text-align:center; font-family:'IBM Plex Sans',sans-serif; font-size:13px; font-weight:500; color:#080327; width:100%; max-width:280px; box-sizing:border-box;">Main flow resumes</div>
</div>

### Two types of Rasa sub-agents
 
Rasa ships two types. The difference is how they signal completion.
 
<div style="margin: 32px 0;">
<style>
  .types-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  .type-card {
    background: #fff;
    border-radius: 8px;
    padding: 20px;
    border: 1px solid #dfe8ff;
    border-top: 3px solid #dfe8ff;
  }
  .type-card.active { border-top-color: #5a17ee; }
  .type-badge {
    display: inline-block;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 20px;
    margin-bottom: 14px;
    font-family: 'IBM Plex Sans', sans-serif;
  }
  .badge-this { background: #EFF1FF; color: #5a17ee; border: 1px solid #DADCFB; }
  .badge-other { background: #EFF1FF; color: #7e7af4; border: 1px solid #DADCFB; }
  .type-name { color: #080327; font-size: 15px; font-weight: 600; margin-bottom: 8px; font-family: 'IBM Plex Sans', sans-serif; }
  .type-desc { color: #636C85; font-size: 13px; line-height: 1.6; margin-bottom: 14px; font-family: 'IBM Plex Sans', sans-serif; }
  .type-row { display: flex; flex-direction: column; gap: 8px; }
  .type-item { display: flex; gap: 10px; align-items: flex-start; }
  .type-dot { width: 6px; height: 6px; border-radius: 50%; margin-top: 5px; flex-shrink: 0; }
  .dot-purple { background: #5a17ee; }
  .dot-green { background: #7e7af4; }
  .type-item-text { color: #080327; font-size: 12px; line-height: 1.5; font-family: 'IBM Plex Sans', sans-serif; }
  .type-completion {
    margin-top: 16px;
    padding: 10px 14px;
    border-radius: 4px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
  }
  .comp-purple { background: #EFF1FF; color: #5a17ee; border-left: 3px solid #5a17ee; }
  .comp-green { background: #EFF1FF; color: #7e7af4; border-left: 3px solid #7e7af4; }
  @media (max-width: 500px) { .types-grid { grid-template-columns: 1fr; } }
</style>
<div class="types-grid">
  <div class="type-card active">
    <div class="type-badge badge-this">This course</div>
    <div class="type-name">General-purpose</div>
    <div class="type-desc">Handles open-ended tasks. The prompt-driven agent loop runs until the sub-agent explicitly signals completion.</div>
    <div class="type-row">
      <div class="type-item">
        <div class="type-dot dot-purple"></div>
        <div class="type-item-text">Exploratory conversations: product advice, loan guidance, option comparisons</div>
      </div>
      <div class="type-item">
        <div class="type-dot dot-purple"></div>
        <div class="type-item-text"> Language model decides when the Sub-agent task is done</div>
      </div>
      <div class="type-item">
        <div class="type-dot dot-purple"></div>
        <div class="type-item-text">Closes with a natural message to the user</div>
      </div>
    </div>
    <div class="type-completion comp-purple">Completes via: task_completed tool</div>
  </div>
  <div class="type-card">
    <div class="type-badge badge-other">Extension</div>
    <div class="type-name">Task-specific</div>
    <div class="type-desc">Designed for structured data collection. Completes automatically when the exit conditions are met.</div>
    <div class="type-row">
      <div class="type-item">
        <div class="type-dot dot-green"></div>
        <div class="type-item-text">Structured tasks: i.e. form filling</div>
      </div>
      <div class="type-item">
        <div class="type-dot dot-green"></div>
        <div class="type-item-text">Fills specific slots; exit conditions define "done"</div>
      </div>
      <div class="type-item">
        <div class="type-dot dot-green"></div>
        <div class="type-item-text">Completes silently; main flow continues immediately</div>
      </div>
    </div>
    <div class="type-completion comp-green">Completes via: exit_if conditions</div>
  </div>
</div>
</div>

>Sub-agents are in beta, available from Rasa 3.14.0.

