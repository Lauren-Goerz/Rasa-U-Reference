### What you built
 
The main agent now orchestrates. It runs `consult_financial_advisor`, passes control to `financial_advisor`, and waits. The sub-agent handles the conversation, then calls `task_completed` with a natural closing message. Control returns to the main flow and the conversation ends cleanly.
 
| File | Role |
|------|------|
| `sub_agents/financial_advisor/config.yml` | Sub-agent definition: name, LLM, MCP connection |
| `endpoints.yml` (`mcp_servers:`) | Registers the MCP server address |
| `data/basics/consult_financial_advisor.yml` | Flow that delegates via `call: financial_advisor` |
 
That is the complete pattern. One sub-agent. One flow. One registered server. Everything else in Chapter 6 is this pattern, extended.
 
---
 
### Knowledge check
 
{Check It!|assessment}(multiple-choice-501060100)
 
{Check It!|assessment}(multiple-choice-501060101)
 
{Check It!|assessment}(multiple-choice-501060102)
 
{Check It!|assessment}(multiple-choice-501060103)
 
 
---
 
### What's next
 
Your `chapter6/` agent is one main agent plus a general-purpose prompt-driven sub-agent with MCP tools. Natural extensions:
 
- **More sub-agents.** Add a folder, register an MCP server, add a flow. The pattern is the same.
- **Task-specific sub-agents.** Use `exit_if` conditions where the task is structured and you want the sub-agent to complete automatically. (i.e. booking an appointment)
- **Slot handback.** A general-purpose sub-agent can return values to the main flow via slots for downstream steps.
- **External sub-agents.** The A2A protocol connects to agents outside your Rasa project entirely.
Rasa docs: [Sub-agents](https://rasa.com/docs/reference/config/agents/react-sub-agents/)
 