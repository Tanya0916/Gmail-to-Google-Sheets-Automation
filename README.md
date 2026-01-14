#  Gmail to Google Sheets Automation

This project automates the process of **extracting emails from Gmail and storing structured data into Google Sheets**.  
It is useful for tracking leads, applications, alerts, or any recurring email-based information.

---

##  Features
- Connects securely to Gmail using Google API
- Reads emails based on:
  - Sender
  - Subject
  - Labels
  - Date range
- Extracts relevant email content
- Automatically updates Google Sheets
- Eliminates manual copy-paste work

---

##  Technologies Used
- Programming Language: Python
- Google APIs:
  - Gmail API
  - Google Sheets API
- Authentication: OAuth 2.0
- Libraries:
  - `google-api-python-client`
  - `google-auth`
  - `google-auth-oauthlib`
  - `pandas`

---

## Project Workflow
1. Authenticate Gmail and Google Sheets access
2. Fetch emails matching given criteria
3. Parse required data (sender, subject, body, date)
4. Store data row-wise into Google Sheets

---



