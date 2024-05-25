from flask import Flask, request, jsonify
from flask_mail import Mail
from mail import Email
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(dotenv_path=find_dotenv())

app = Flask(__name__)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_PROVIDER_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PROVIDER_PORT')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_PROVIDER_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PROVIDER_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def send_email(data):
    sender = os.environ.get('MAIL_SENDER')
    recipients =  data['recipients']
    subject = data['subject']
    body = data['body']

    email = Email()
    results = email.send(mail, sender, recipients, subject, body)

    return results

@app.route("/send-email", methods=['POST'])
def post():
    data = request.json
    res = send_email(data)
    return res

@app.route("/send-email", methods=['GET'])
def get():
    return jsonify({"status": "success", "message": "App is running"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)