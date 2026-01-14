import base64
from email import message_from_bytes

def parse_email(service, msg_id):
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    payload = msg['payload']
    headers = payload['headers']

    sender = next(h['value'] for h in headers if h['name'] == 'From')
    subject = next(h['value'] for h in headers if h['name'] == 'Subject')
    date = next(h['value'] for h in headers if h['name'] == 'Date')

    body = ""
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
    else:
        body = base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')

    return [sender, subject, date, body]
