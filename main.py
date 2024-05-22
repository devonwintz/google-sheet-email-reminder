import os
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv, find_dotenv
from utils import convert_google_sheet_url, send_email

load_dotenv(dotenv_path=find_dotenv())

def load_data(url):
    df = pd.read_csv(convert_google_sheet_url(url))
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def main():
    google_sheet_url = os.environ.get('GOOGLE_SHEET_URL')
    mailing_route = os.environ.get('MAILING_ROUTE')

    df = load_data(google_sheet_url)
    current_date = datetime.now()

    for _, row in df.iterrows():
        target_date = row['Date'] - timedelta(days=row['Advance Notice Days'])
        max_allowed_date = current_date + timedelta(days=row['Advance Notice Days'])

        if current_date <= target_date <= max_allowed_date and row['Email Status'] == 'Not Sent':
            date = row['Date'].strftime('%Y-%m-%d')
            recipients_list = [recipient.strip() for recipient in row['Recipients'].split(',')]
            days_until_due = (row['Date'] - current_date).days

            payload = {
                'subject': row['Description'],
                'recipients': recipients_list,
                'body': f"This email serves to inform you that '{row['Description']}' is due in {days_until_due} day(s) on {date}"
            }

            send_email(payload, mailing_route)

if __name__ == "__main__":
    main()