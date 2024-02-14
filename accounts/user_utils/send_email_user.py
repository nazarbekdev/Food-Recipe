import os
import smtplib
import time
from email.mime.text import MIMEText
from dotenv import load_dotenv
from config.celery import app

load_dotenv()


@app.task
def send_mail(data):
    start = time.time()
    msg = MIMEText(data['email_body'])
    msg['Subject'] = data['email_subject']
    msg['From'] = os.getenv('FROM_EMAIL')
    msg['To'] = data['to_email']
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(os.getenv('FROM_EMAIL'), os.getenv('EMAIL_PASSWORD'))
       smtp_server.sendmail(from_addr=os.getenv('FROM_EMAIL'), to_addrs=data['to_email'], msg=msg.as_string())
    print("Message sent!")
    print(time.time() - start)

