from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from Accounts import Authorizations

body_message = '''
BODY
'''

message = MIMEMultipart()
message["from"] = "Justin A."
message["to"] = "targetemail@target.com"
message["subject"] = "TEST"
message.attach(MIMEText(body_message, "plain"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(Authorizations.user, Authorizations.pword)
    smtp.send_message(message)
    print("Task Completed, message is sent")
