import argparse
from datetime import datetime, timedelta
from dateutil import parser as date_parser
from calendar_checker import check_upcoming_meetings, get_all_upcoming_meetings, create_event, delete_event

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

def get_current_meeting():
    now = datetime.now()
    today = now.date()
    meetings = check_upcoming_meetings(today)["meetings"]
    for m in meetings:
        try:
            # Only consider meetings with a specific time
            if m["start"] != "All day":
                start_time = datetime.strptime(f"{today} {m['start']}", "%Y-%m-%d %H:%M")
                end_time = start_time + timedelta(hours=1)  # Assume 1 hour duration
                if start_time <= now < end_time:
                    return m
        except Exception as e:
            continue
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check or create Google Calendar events.")
    # Arguments for checking meetings
    parser.add_argument("--date", type=str, help="Check meetings for a specific date (e.g., 'today', 'tomorrow', '2025-07-01').")
    parser.add_argument("--all", action="store_true", help="Show all upcoming meetings.")
    parser.add_argument("--current", action="store_true", help="Show the current meeting (if any).")
    parser.add_argument("--show-ids", action="store_true", help="Show event IDs in the output.")

    # Arguments for creating a meeting
    parser.add_argument("--create", action="store_true", help="Create a new event.")
    parser.add_argument("--summary", type=str, help="The summary (title) of the event.")
    parser.add_argument("--start", type=str, help="Start time in 'YYYY-MM-DD HH:MM' format.")
    parser.add_argument("--end", type=str, help="End time in 'YYYY-MM-DD HH:MM' format.")
    parser.add_argument("--desc", type=str, help="Optional description for the event.")

    # Argument for deleting an event
    parser.add_argument("--delete", type=str, help="Delete an event by its ID.")

    args = parser.parse_args()

    if args.delete:
        delete_event(args.delete)

    elif args.create:
        if not args.summary or not args.start or not args.end:
            print("❌ Error: --summary, --start, and --end are required to create an event.")
            exit(1)
        
        start_utc = date_parser.parse(args.start).isoformat()
        end_utc = date_parser.parse(args.end).isoformat()
        
        created = create_event(args.summary, start_utc, end_utc, args.desc)
        if created:
            print(f"✅ Event created successfully: {created.get('summary')} ({created.get('htmlLink')})")

    elif args.current:
        current = get_current_meeting()
        if current:
            print(f"🟢 Current meeting: {current['summary']} at {current['start']}")
        else:
            print("❌ No meeting is currently in progress.")
    elif args.all:
        meetings = get_all_upcoming_meetings()
        if not meetings["meetings"]:
            print("✅ You have no upcoming meetings.")
        else:
            print("📅 Your upcoming meetings:")
            for m in meetings["meetings"]:
                if args.show_ids:
                    print(f"- {m['summary']} at {m['start']} (ID: {m['id']})")
                else:
                    print(f"- {m['summary']} at {m['start']}")
    else:
        target_date = resolve_target_date(args.date)
        meetings = check_upcoming_meetings(target_date)
        if not meetings["meetings"]:
            print(f"✅ You have no meetings on {target_date}.")
        else:
            print(f"📅 Your meetings on {target_date}:")
            for m in meetings["meetings"]:
                if args.show_ids:
                    print(f"- {m['summary']} at {m['start']} (ID: {m['id']})")
                else:
                    print(f"- {m['summary']} at {m['start']}")

