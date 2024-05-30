## Google Sheet Email Reminder

This project provides a simple way to set up email reminders based on data from a Google Sheet. Please note that this implementation requires your Google Sheet to be public and does not use recommended authentication methods. Make sure your sheet does not contain sensitive data.

### Table Structure

The Google Sheet should have the following table structure:

| ID | Description | Date | Advance Notice Days | Recipients | Email Status |
|----|-------------|------|---------------------|------------|--------------|
|    |             |      |                     |            |              |

### Usage

1. **Google Sheet Setup**: Create a Google Sheet with the specified table structure. Populate the sheet with your data, including the description, date, advance notice days, recipients, and email status.

2. **Advance Notice Days**: The "Advance Notice Days" column lets you specify how many days in advance you want to receive an email reminder by entering comma-separated values. For instance, if you enter "7,1", you will receive email reminders 7 days and 1 day before the specified date.

3. **Recipients**: Enter the email addresses of the recipients in the "Recipients" column. Separate multiple email addresses with commas.

4. **Email Status**: Use the "Email Status" column to track whether an email reminder has been sent. Set it to "Not Sent" initially.

5. **Run the Script**: Run the provided Python script to read data from the Google Sheet, calculate the dates for reminders, and send email notifications.

6. **Automate with a Scheduler**: You can automate the process of sending reminders by setting up a scheduler to run the Python script at specified intervals.
    - **Unix-based Systems (Using `cron`)**: Open your terminal, type `crontab -e`, and add a new line specifying the schedule and command to run your Python script.
    - **Windows (Using Task Scheduler)**: Open Task Scheduler, create a new basic task, specify the trigger and action to run your Python script.

7. **Email Reminder**: Once the script is set up and running, you will receive email reminders based on the specified advance notice days.

### Disclaimer

This implementation does not use recommended authentication methods and relies on the Google Sheet being public. Ensure that your Google Sheet does not contain sensitive data before using this method.

### Notes

This implementation operates similarly to setting reminders on a calendar, but instead of receiving notifications, you will receive email reminders.
