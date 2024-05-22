from flask import render_template
from flask_mail import Message

class Email(object):
    def send(self, mail, sender, recipients, subject, body):
        try:
            msg = Message(subject=subject, sender=sender, recipients=recipients)
            msg.body = body
            msg.html = render_template('generic_notification.html', body=body)

            mail.send(msg)

            results = {
                'status': 'success',
                'message': 'Email was sent successfully'
            }
        except Exception as e:
            results = {
                'status': 'error',
                'message': f'Failed to send email: {str(e)}'
            }

        return results