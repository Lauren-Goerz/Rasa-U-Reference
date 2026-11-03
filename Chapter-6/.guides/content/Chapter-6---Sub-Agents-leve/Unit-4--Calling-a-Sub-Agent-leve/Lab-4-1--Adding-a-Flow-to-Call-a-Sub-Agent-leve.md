<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Add the flow that will call the new appointment booking sub-agent.

In Rasa, we are able to orchestrate to sub-agents by defining them within a flow. The description of this flow helps Rasa route to it at the right moment, and it has one step to call the sub-agent: `call: branch_appointment_booking`. 

When the sub-agent finishes, it sends its own natural closing message via `task_completed` and hands back to the central agent. No further follow-up action is needed in this case, however since the sub-agent is called within a flow, you can layer hard-coded steps around it if necessary. 

The `name` and `description` directly affect how the command generator (currently `SearchReadyLLMCommandGenerator`) routes conversations. A good description is specific about when this flow should be activated, and when it should not.

 
## Steps:
Copy the YAML below to a new flow, `chapter6/data/basics/book_appointment.yml` and Save.
 
```yaml
flows:
  book_appointment:
    name: "Book an appointment at the branch"
    description: |
      Start this flow when the user wants to book, schedule, or arrange an
      appointment with a financial advisor at the branch. Not for balance
      checks, transfers, or general financial questions.
    steps:
      - call: branch_appointment_booking
```
 
Feel free to adjust both values. The description is worth spending time on, the more precisely it defines the boundary between this flow and `check_balance` or `hours`, the more reliably the command generator routes to the right place.

## Verify

{Check It!|assessment}(code-output-compare-501060003)