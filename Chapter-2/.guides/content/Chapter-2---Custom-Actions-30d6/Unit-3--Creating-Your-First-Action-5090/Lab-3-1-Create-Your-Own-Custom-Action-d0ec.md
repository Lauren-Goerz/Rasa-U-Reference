<p style="font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#5a17ee;margin:0 0 4px;">Lab objective</p>

Build `action_holiday_hours`: a custom action that checks today's date. 

If today is a public holiday, it tells the user the bank is closed. Otherwise it returns the general holiday schedule.
 
---
 
**1. Fill in the blanks**
 
Use `action_bank_hours.py` as a reference. The structure is identical: import `datetime`, inherit from `Action`, implement `name()` and `run()`.
 
{Check It!|assessment}(fill-in-the-blanks-201030010)
 
---
 
**2. Save the file**
 
1. Open `chapter2/actions/` in the file tree.
2. Create a new file named `action_holiday_hours.py`.
3. Paste your completed script from Step 1.
4. Save.
---
 
**3. Run the assessment**
 
The grader checks that the file contains the correct structure: `ActionHolidayHours`, `name()` returning `"action_holiday_hours"`, `datetime`-based logic, and a `dispatcher.utter_message()` call.
 
{Check It!|assessment}(code-output-compare-2266471391)
 
---
 
When Rasa reaches an action step in a flow, this is what happens:
 
```text
Flow step: - action: action_holiday_hours
  ↓
Rasa sends request to the action server
  ↓
Action server finds ActionHolidayHours
  ↓
Calls name() to verify the registered name matches
  ↓
Calls run()
  ↓
dispatcher.utter_message() sends the reply
  ↓
Action returns []
  ↓
Flow continues to the next step
```