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
    email_sent = False
    google_sheet_url = os.environ.get('GOOGLE_SHEET_URL')
    mailing_route = os.environ.get('MAILING_ROUTE')

    df = load_data(google_sheet_url)
    current_date_time = datetime.now()
    current_date = current_date_time.replace(hour=0, minute=0, second=0, microsecond=0)

    for _, row in df.iterrows():
        advance_notice_days = [int(advance_notice_day.strip()) for advance_notice_day in str(row['Advance Notice Days']).split(',')]

        for advance_notice_day in advance_notice_days:
            target_date = row['Date'] - timedelta(days=advance_notice_day)

            if current_date == target_date and row['Email Status'] == 'Not Sent':
                email_sent = True
                date = row['Date'].strftime('%Y-%m-%d')
                recipients_list = [recipient.strip() for recipient in row['Recipients'].split(',')]
                days_until_due = (row['Date'] - current_date).days

                payload = {
                    'subject': row['Description'],
                    'recipients': recipients_list,
                    'body': (f"This email serves to inform you that '{row['Description']}' "
                    f"is due {'today.' if days_until_due == 0 else f'in {days_until_due} day(s) on {date}.'}")
                }
                send_email(payload, mailing_route)

    if not email_sent:
        print("No email to be dispatched")

if __name__ == "__main__":
    main()