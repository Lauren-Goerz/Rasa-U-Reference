Up until now, you have only used custom actions: Python functions exposed by the Rasa action server and called directly by flows. The MCP server is new in chapter 6. It exposes functions as tools that a sub-agent's LLM can call during its reasoning loop. Both are separate processes that expose functions, but they work in completely different ways.
 
| | Action server | MCP server |
|---|--------------|------------|
| **Who calls it** | The flow, at a defined `action:` step | The sub-agent's LLM, during its agent reasoning loop |
| **How many times** | Once per step | As many times as needed, in any order |
| **Who decides when** | You do — by writing the flow | The LLM does, based on the conversation |
| **Protocol** | Rasa-specific | MCP (open standard, any compatible client can connect) |
| **In this course** | `action_check_balance_simple`, `action_process_transfer` | `get_account_options`, `get_current_rates`, `calculate_loan_repayment` |
| **Used by** | Main agent | `financial_advisor` sub-agent |
### How they fit together
 
<div style="background:#EFF1FF; border-radius:12px; padding:28px 20px; border:1px solid #dfe8ff; margin:32px 0;">
<table style="width:100%; border-collapse:collapse; table-layout:fixed;"><tr>
<td style="width:50%; padding:0 8px 0 0; vertical-align:bottom; text-align:center;">
<div style="background:#fff; border:1px solid #5a17ee; border-radius:8px; padding:10px 16px; margin-bottom:6px;"><span style="font-family:'IBM Plex Sans',sans-serif; font-size:12px; font-weight:600; color:#080327;">Main agent</span></div>
<div style="color:#A6AAF3; font-size:16px; line-height:1.4;">↓</div>
<div style="font-family:'IBM Plex Sans',sans-serif; font-size:10px; color:#5a17ee; font-weight:600; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:2px;">action: step</div>
<div style="color:#A6AAF3; font-size:16px; line-height:1.4;">↓</div>
</td>
<td style="width:50%; padding:0 0 0 8px; vertical-align:bottom; text-align:center;">
<div style="background:#fff; border:1px solid #5a17ee; border-radius:8px; padding:10px 16px; margin-bottom:6px;"><span style="font-family:'IBM Plex Sans',sans-serif; font-size:12px; font-weight:600; color:#080327;">Main agent</span></div>
<div style="color:#A6AAF3; font-size:16px; line-height:1.4;">↓</div>
<div style="font-family:'IBM Plex Sans',sans-serif; font-size:10px; color:#5a17ee; font-weight:600; letter-spacing:0.08em; text-transform:uppercase; margin-bottom:2px;">call: step</div>
<div style="color:#A6AAF3; font-size:16px; line-height:1.4;">↓</div>
</td>
</tr><tr>
<td style="padding:0 8px 0 0; vertical-align:bottom; text-align:center;"></td>
<td style="padding:0 0 0 8px; vertical-align:bottom; text-align:center;">
<div style="background:#DADCFB; border:1px solid #7e7af4; border-radius:8px; padding:10px 16px; margin-bottom:6px;">
<div style="font-family:'IBM Plex Sans',sans-serif; font-size:12px; font-weight:600; color:#080327;">branch_appointment_booker</div>
<div style="font-family:'IBM Plex Sans',sans-serif; font-size:10px; color:#636C85;">sub-agent · Agent loop</div>
</div>
<div style="color:#A6AAF3; font-size:16px; line-height:1.4;">↓</div>
</td>
</tr><tr>
<td style="padding:0 8px 0 0; vertical-align:top;">
<div style="background:#fff; border:1px solid #dfe8ff; border-radius:8px; padding:12px; text-align:left;">
<div style="font-family:'IBM Plex Sans',sans-serif; font-size:12px; font-weight:600; color:#080327; margin-bottom:8px;">Action server</div>
<div style="font-family:'IBM Plex Mono',monospace; font-size:10px; color:#636C85; line-height:2;">action_check_balance_simple<br>action_process_transfer</div>
</div>
</td>
<td style="padding:0 0 0 8px; vertical-align:top;">
<div style="background:#fff; border:1px solid #dfe8ff; border-radius:8px; padding:12px; text-align:left;">
<div style="font-family:'IBM Plex Sans',sans-serif; font-size:12px; font-weight:600; color:#080327; margin-bottom:8px;">MCP server</div>
<div style="font-family:'IBM Plex Mono',monospace; font-size:10px; color:#636C85; line-height:2;">get_appointment_availability</div>
</div>
</td>
</tr></table>
<table style="width:100%; border-collapse:collapse; table-layout:fixed; margin-top:16px;"><tr>
<td style="width:50%; padding:0 8px 0 0; vertical-align:top;">
<div style="background:#fff; border:1px solid #dfe8ff; border-top:3px solid #5a17ee; border-radius:8px; padding:12px;">
<div style="font-family:'IBM Plex Sans',sans-serif; font-size:11px; font-weight:600; color:#5a17ee; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:6px;">Action server</div>
<div style="font-family:'IBM Plex Sans',sans-serif; font-size:12px; color:#636C85; line-height:1.6;">Called by the flow at a defined step. Runs once, returns, flow continues. The LLM does not choose when it runs.</div>
</div>
</td>
<td style="width:50%; padding:0 0 0 8px; vertical-align:top;">
<div style="background:#fff; border:1px solid #dfe8ff; border-top:3px solid #7e7af4; border-radius:8px; padding:12px;">
<div style="font-family:'IBM Plex Sans',sans-serif; font-size:11px; font-weight:600; color:#7e7af4; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:6px;">MCP server</div>
<div style="font-family:'IBM Plex Sans',sans-serif; font-size:12px; color:#636C85; line-height:1.6;">Called by the LLM during reasoning. Can be called multiple times, in any order, until the task is done.</div>
</div>
</td>
</tr></table>
</div>

### Running both together

The action server and MCP server are separate processes that can run in parallel alongside Rasa. Each handles the part of the system it is designed for, one does not replace the other.
  
