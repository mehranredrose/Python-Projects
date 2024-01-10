from email.mime.text import MIMEText
from local_config import MAILGUN_APIKEY
import smtplib
import requests

from config import rules
RECEIVER_EMAIL = rules['email']['receiver']


def send_smtp_email(subject, body):
    msg = MIMEText(body)
    msg['Subject']: subject
    msg['From']: "s"
    msg['To']: RECEIVER_EMAIL

    with smtplib.SMTP('smtp.mailgun.org', 587)as mail_server:
        mail_server.login('', MAILGUN_APIKEY)
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
        mail_server.quit()


def send_api_mail(subject, body):
    return requests.post(
        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", MAILGUN_APIKEY),
        data={"from": "Excited User mailgun@redrose.mydomain.com",
              "to": [RECEIVER_EMAIL],
              "subject": subject,
              "text": body})
