from googleapiclient.discovery import build
from auth import get_credentials

# Check up to 10 unread emails in the inbox
def check_unread_emails():
    creds = get_credentials()  # Should include Gmail scope
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX', 'UNREAD'], maxResults=10).execute()
    messages = results.get('messages', [])
    emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = msg_data.get('snippet', '')
        subject = ''
        for header in msg_data['payload']['headers']:
            if header['name'] == 'Subject':
                subject = header['value']
                break
        emails.append({'subject': subject, 'snippet': snippet})
    return emails

if __name__ == "__main__":
    emails = check_unread_emails()
    if not emails:
        print("✅ You have no unread emails.")
    else:
        print("📧 Your unread emails:")
        for i, email in enumerate(emails, 1):
            print(f"{i}. Subject: {email['subject']}")
            print(f"   Snippet: {email['snippet'][:100]}\n")
