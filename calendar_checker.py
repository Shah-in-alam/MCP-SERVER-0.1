from googleapiclient.discovery import build
from datetime import datetime, timezone
from auth import get_credentials

def check_upcoming_meetings(target_date):
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=20,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    meetings = []

    for event in events:
        start_raw = event['start'].get('dateTime', event['start'].get('date'))
        try:
            if 'T' in start_raw:
                start_obj = datetime.fromisoformat(start_raw.replace('Z', '+00:00'))
                time_str = start_obj.strftime('%H:%M')
            else:
                start_obj = datetime.fromisoformat(start_raw)
                time_str = "All day"

            if start_obj.date() == target_date:
                meetings.append({
                    "summary": event.get('summary', 'No Title'),
                    "start": time_str
                })
        except Exception as e:
            print("❌ Failed to parse date:", start_raw, "| Error:", e)
            continue

    return {"meetings": meetings}

# New function to get all upcoming meetings

def get_all_upcoming_meetings():
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    events_result = service.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=50,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    meetings = []

    for event in events:
        start_raw = event['start'].get('dateTime', event['start'].get('date'))
        try:
            if 'T' in start_raw:
                start_obj = datetime.fromisoformat(start_raw.replace('Z', '+00:00'))
                time_str = start_obj.strftime('%Y-%m-%d %H:%M')
            else:
                start_obj = datetime.fromisoformat(start_raw)
                time_str = start_obj.strftime('%Y-%m-%d') + " (All day)"

            meetings.append({
                "summary": event.get('summary', 'No Title'),
                "start": time_str
            })
        except Exception as e:
            print("❌ Failed to parse date:", start_raw, "| Error:", e)
            continue

    return {"meetings": meetings}

