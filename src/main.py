from gmail_service import get_unread_emails
from sheets_service import append_to_sheet
from email_parser import parse_email

def main():
    print(" Starting Gmail → Sheets automation...")

    # Step 1: Fetch unread emails
    emails = get_unread_emails()
    print(f"Fetched {len(emails)} unread emails.")

    # Step 2: Parse and append each email
    for email in emails:
        parsed = parse_email(email)
        append_to_sheet([parsed['sender'], parsed['subject'], parsed['date'], parsed['body']])
        print(f"Appended email from {parsed['sender']} to Google Sheet.")

    print("Process complete!")

if __name__ == "__main__":
    main()



