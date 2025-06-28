from datetime import datetime, timezone
from calendar_checker import check_upcoming_meetings
from email_checker import check_unread_emails

def print_daily_summary():
    # Get today's date
    today = datetime.now(timezone.utc).date()
    # Get meetings
    meetings_data = check_upcoming_meetings(today)
    meetings = meetings_data.get('meetings', [])
    # Get unread emails
    emails = check_unread_emails()

    print(f"===== Daily Summary for {today} =====\n")
    # Meetings
    if not meetings:
        print("✅ You have no meetings today.\n")
    else:
        print("📅 Your meetings today:")
        for m in meetings:
            print(f"- {m['summary']} at {m['start']}")
        print()
    # Emails
    if not emails:
        print("✅ You have no unread emails.")
    else:
        print("📧 Your unread emails:")
        for i, email in enumerate(emails, 1):
            print(f"{i}. Subject: {email['subject']}")
            print(f"   Snippet: {email['snippet'][:100]}\n")

if __name__ == "__main__":
    print_daily_summary() 