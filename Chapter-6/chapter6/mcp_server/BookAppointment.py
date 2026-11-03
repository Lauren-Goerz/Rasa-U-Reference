"""
Appointment Booking MCP server for Level 6 (Streamable HTTP — required by Rasa's MCP client).

Run from level6:
  python mcp_server/BookAppointment.py

Default URL for endpoints.yml:
  http://127.0.0.1:8080/mcp
"""
import asyncio
import json
import sys
from datetime import datetime, timedelta

from mcp.server.fastmcp import FastMCP

PORT = 8080
STREAMABLE_PATH = "/mcp"

mcp = FastMCP(
    "AppointmentBooking",
    instructions="Appointment scheduling tools for the Level 6 branch appointment sub-agent.",
    host="0.0.0.0",
    port=PORT,
    streamable_http_path=STREAMABLE_PATH,
)


def _as_json(obj) -> str:
    return json.dumps(obj, ensure_ascii=False)


def _is_holiday(date: datetime) -> str | None:
    """Return holiday name if the date is a bank holiday, otherwise None."""
    holidays = {
        (1, 1):   "New Year's Day",
        (7, 4):   "Independence Day",
        (12, 25): "Christmas Day",
    }
    return holidays.get((date.month, date.day))


# Fixed availability pattern per weekday (0=Monday ... 4=Friday)
SLOT_AVAILABILITY = {
    0: {"9:00 AM": True,  "10:00 AM": False, "11:00 AM": True,  "1:00 PM": False, "2:00 PM": True,  "3:00 PM": True,  "4:00 PM": False},
    1: {"9:00 AM": False, "10:00 AM": True,  "11:00 AM": False, "1:00 PM": True,  "2:00 PM": False, "3:00 PM": True,  "4:00 PM": True },
    2: {"9:00 AM": True,  "10:00 AM": True,  "11:00 AM": False, "1:00 PM": False, "2:00 PM": True,  "3:00 PM": False, "4:00 PM": True },
    3: {"9:00 AM": False, "10:00 AM": True,  "11:00 AM": True,  "1:00 PM": True,  "2:00 PM": False, "3:00 PM": True,  "4:00 PM": False},
    4: {"9:00 AM": True,  "10:00 AM": False, "11:00 AM": True,  "1:00 PM": False, "2:00 PM": True,  "3:00 PM": False, "4:00 PM": True },
}


@mcp.tool()
def get_available_slots() -> str:
    """
    Get available appointment slots for the next 3 open business days.
    The bank is open Monday to Friday, 9:00 AM to 5:00 PM.
    Closed on weekends and major public holidays.
    Not all slots are available — some are already booked.
    Call this once at the start before asking the user to choose a time.
    """
    now = datetime.now()
    slots = []
    day = now
    count = 0

    while count < 3:
        day = day + timedelta(days=1)
        if day.weekday() >= 5:
            continue
        holiday = _is_holiday(day)
        if holiday:
            slots.append({
                "date": day.strftime("%A, %d %B %Y"),
                "available_times": [],
                "note": f"Closed — {holiday}"
            })
            count += 1
            continue
        available = [
            time for time, free in SLOT_AVAILABILITY[day.weekday()].items() if free
        ]
        slots.append({
            "date": day.strftime("%A, %d %B %Y"),
            "available_times": available,
            "note": f"{len(available)} of 7 slots available"
        })
        count += 1

    return _as_json({
        "today": now.strftime("%A, %d %B %Y"),
        "bank_hours": "Monday to Friday, 9:00 AM - 5:00 PM",
        "available_slots": slots
    })


@mcp.tool()
def book_appointment(date: str, time: str, name: str) -> str:
    """
    Book an appointment with a financial advisor.
    date: the chosen date (e.g. "Monday, 13 May 2025")
    time: the chosen time — must be one of the available times from get_available_slots
    name: the customer's full name
    Only call this after the user has confirmed a date, time, and their name.
    """
    reference = "FA-" + str(abs(hash(f"{date}{time}{name}")) % 10000).zfill(4)
    return _as_json({
        "confirmed": True,
        "name": name,
        "date": date,
        "time": time,
        "reference": reference,
        "notes": "Please bring valid ID. Call 1-800-BANK-123 to reschedule."
    })


async def _run() -> None:
    print(
        f"Appointment Booking MCP (Streamable HTTP)\n"
        f"URL for endpoints.yml:\n  http://127.0.0.1:{mcp.settings.port}{STREAMABLE_PATH}",
        flush=True,
    )
    await mcp.run_streamable_http_async()


def main() -> None:
    port = PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    mcp.settings.port = port
    asyncio.run(_run())


if __name__ == "__main__":
    main()