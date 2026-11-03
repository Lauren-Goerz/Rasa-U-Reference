<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Setup the sub-agent and prompt so that it can use the mcp server we just enabled. 

In order to make a sub-agent work, it needs its own `config.yml`. Similar to the global config.yml, this tells Rasa who the sub-agent is, which LLM it uses, and which MCP server it connects to. Three of these values must match exactly what is defined in other files.


## Step 1: 
Create chapter6/sub_agents/branch_appointment_booking/config.yml. Paste in the template `config.yml` of an appointment booking sub-agent you can use with the appointment_mcp server. 

 
```yaml
agent:
  name: branch_appointment_booking          # must match `call:` in Lab 4.1
  protocol: RASA
  description: |
    You are a friendly appointment scheduler for a banking branch.
 
    Step 1: Call get_available_slots once at the start. Do not call it again.
    Remember the result — you will use it for the rest of the conversation.
 
    Step 2: Present the available dates and times conversationally. Do not
    list everything at once. Let the user guide the negotiation. If they ask
    for a date or time that is not available, tell them and suggest the
    nearest alternative from the data you already have.
 
    Step 3: Once the user agrees on a date and time, ask for their full name.
 
    Step 4: Call book_appointment with the confirmed date, time, and name.
    This step is mandatory. Do not skip it.
 
    Step 5: Confirm the booking reference number and call task_completed.
 
configuration:
  llm:
    model_group: openai-gpt-5-mini  # must match a model_groups id in endpoints.yml
 
connections:
  mcp_servers:
    - name: appointment_mcp         # must match the mcp_servers entry registered in Lab 6.2.2
      include_tools:
        - get_available_slots
        - book_appointment
```
 
| Field | Connects to |
|-------|-------------|
| `agent.name: branch_appointment_booking` | Must match `call:` in a flow |
| `configuration.llm.model_group` | Must match a `model_groups` `id` in `endpoints.yml` |
| `connections.mcp_servers.name` | Must match the MCP server registered in Lab 6.2.1 |
 
**The `description` field** is the sub-agent's system prompt. The LLM follows it at runtime. Be specific about when to call each tool and when to call `task_completed`. Appointment booking is a great candidate for a sub-agent because booking an appointment is often like a negotiation, two parties have to flexibly navigate to align on a time, and the number of turns it takes to do this will always vary. 
 
## Verify  
{Check It!|assessment}(code-output-compare-501060001)