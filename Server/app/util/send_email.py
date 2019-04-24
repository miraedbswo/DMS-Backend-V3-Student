import sendgrid
import os
from sendgrid.helpers.mail import *

import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>JoinCode</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<div style="height:100vh; display:flex; justify-content:center; align-items:center; 
        font-family: 'NanumSquare'; src:url('https://cdn.rawgit.com/hiun/NanumSquare/master/nanumsquare.css');">
    <div style="width:80%;height:80%">
        <img src="https://s3.ap-northeast-2.amazonaws.com/dsm-dms/dms_logo.png" alt="logo" style="
                width:230px;
                height:230px;"> 

        <div id="mainText" style="    
                font-size:60px;
                color:#404040;">Congratulations on joining us.</div>

        <div id="text" style="
                margin-top:45px;;
                font-size:30px;
                color:#9e9e9e;">Enter confirm code to DMS</div>

        <div id="codeBox" style="
                margin-top:75px;
                line-height:165px;  
                text-align:center;
                width:596px;
                height:165px;
                background-color:#19b6b6;
                border-radius:36px; 
                -webkit-border-radius:36px;
                -moz-border-radius:36px;
                -o-border-radius:36px; 
                color:#fff;
                font-size:98px;
                font-weight:bold;
                letter-spacing:20px;">{}</div>

    </div>
</body>
</html>
"""

unsigned_student_list = []
#
msg = MIMEMultipart('alternative')

MAIL_SERVER = 'smtp.mailgun.org'
MAIL_ID = 'dms@istruly.sexy'
MAIL_PW = 'dmsM@ail2019'
MAIL_PORT = 587


def send_email_by_smtp(email: str, verify_code):
    smtp = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
    smtp.starttls()
    smtp.login(MAIL_ID, MAIL_PW)
    a = html.format(verify_code)

    msg.attach(MIMEText(a, 'html'))

    msg['Subject'] = 'Congratulations on joining DMS.'
    msg['To'] = email
    msg['From'] = MAIL_ID
    smtp.sendmail(MAIL_ID, email, msg.as_string())


def send_email_by_sendgrid_api(email: str, verify_code: str):

    msg = html.format(verify_code)
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY', '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'))
    print(os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("dms@dsm.hs.kr")
    to_email = Email(email)
    subject = "Congratulations on joining DMS."
    content = Content("text/html", msg)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    print(response.status_code)
    print(response.body)
    print(response.headers)
