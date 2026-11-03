<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Use two terminals to 1) activate your MCP Server and 2) Test it with Rasa Inspector

Click on the small **terminal icon** in your file tree to open a second terminal. 
- Terminal 1: Runs the MCP server. 
- Terminal 2: Runs `rasa inspect`
 
**Terminal 1: MCP server**
*Make sure your .venv is active*
```bash
cd chapter6
python mcp_server/BookAppointment.py
```
 
You should see:
```
Appointment Booking MCP (Streamable HTTP)
URL for endpoints.yml:
  http://127.0.0.1:8080/mcp
```
 
Keep this running. Navigate to the second terminal tab.
 
**Terminal 2: Rasa**
*Make sure your .venv is active*
```bash
cd chapter6
python -m rasa inspect
```
 
Open the Inspector using the **Rasa Inspect** button in the blue menu at the top of the page.
 
**Demo phrasing.** Use natural appointment booking language:
 
- `I'd like to book an appointment with a financial advisor`
- `Do you have any availability this week for an appointment?`
- `Can I come in to the branch tomorrow?`

Avoid balance checks or transfers as those route to the main agent's existing flows, which is correct behavior.

Keep in mind, this is just a demo, with a more powerful language model the reasoning of your sub-agent will improve. 
 
If you take a look at the tracker in the rasa inspector panel, you should see the main agent start `book_appointment`, the `branch_appointment_booking` sub-agent fetch available slots via MCP, negotiate a time with you, and confirm the booking with a reference number before calling `task_completed`.
 