from src.gmail_service import get_gmail_service, fetch_unread_emails
from src.sheets_service import get_sheets_service, append_row
from src.email_parser import parse_email

def main():
    gmail = get_gmail_service()
    sheets = get_sheets_service()

    messages = fetch_unread_emails(gmail)

    for m in messages:
        row = parse_email(gmail, m['id'])
        append_row(sheets, row)
        # Mark as read
        gmail.users().messages().modify(userId='me', id=m['id'], body={'removeLabelIds': ['UNREAD']}).execute()

if __name__ == "__main__":
    main()
