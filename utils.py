import re
import requests

def convert_google_sheet_url(url):
    """
    Convert your Google Sheets URL into a CSV export URL
    """
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'
    new_url = re.sub(pattern, replacement, url)

    return new_url

def send_email(payload, url):
    response = requests.post(url, headers={'Content-Type': 'application/json'}, json=payload)
    if response.status_code == 200:
        print(f"Email sent successfully: {payload['subject']}")
    else:
        print(f"Failed to send email: {payload['subject']} - {payload}")
