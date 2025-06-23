import argparse
from datetime import datetime, timedelta
from dateutil import parser as date_parser
from calendar_checker import check_upcoming_meetings, get_all_upcoming_meetings

def resolve_target_date(date_input):
    today = datetime.now().date()
    if date_input.lower() == "today":
        return today
    elif date_input.lower() == "tomorrow":
        return today + timedelta(days=1)
    elif date_input.lower() == "yesterday":
        return today - timedelta(days=1)
    else:
        try:
            return date_parser.parse(date_input).date()
        except Exception as e:
            print(f"❌ Invalid date format: {date_input} — {e}")
            exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", type=str, default="tomorrow")
    parser.add_argument("--all", action="store_true", help="Show all upcoming meetings")
    args = parser.parse_args()

    if args.all:
        meetings = get_all_upcoming_meetings()
        if not meetings["meetings"]:
            print("✅ You have no upcoming meetings.")
        else:
            print("📅 Your upcoming meetings:")
            for m in meetings["meetings"]:
                print(f"- {m['summary']} at {m['start']}")
    else:
        target_date = resolve_target_date(args.date)
        meetings = check_upcoming_meetings(target_date)
        if not meetings["meetings"]:
            print(f"✅ You have no meetings on {target_date}.")
        else:
            print(f"📅 Your meetings on {target_date}:")
            for m in meetings["meetings"]:
                print(f"- {m['summary']} at {m['start']}")

