from fastapi import FastAPI,Query
from datetime import datetime,timedelta,timezone
import dateutil.parser
from calendar_checker import check_upcoming_meetings

app = FastAPI()

@app.get("/check-meetings")
def get_meetings():
    try:
        target_date = datetime.now(timezone.utc).date()
        return check_upcoming_meetings(target_date)
    except Exception as e:
        print("❌ Error in /check-meetings:", e)
        return {"error": str(e)}

@app.get("/check-meetings/plain")
def get_meetings_plain(date: str = Query(default="today")):
    try:
        if date.lower() == "today":
            target_date = datetime.now(timezone.utc).date()
        elif date.lower() == "tomorrow":
            target_date = datetime.now(timezone.utc).date() + timedelta(days=1)
        else:
            target_date = dateutil.parser.parse(date).date()

        data = check_upcoming_meetings(target_date)

        if not data['meetings']:
            return f"✅ You have no meetings on {target_date}."

        response = f"📅 Your meetings on {target_date}:\n"
        for m in data['meetings']:
            response += f"• {m['summary']} at {m['start']}\n"
        return response

    except Exception as e:
        print("❌ ERROR:", e)
        return {"error": str(e)}
