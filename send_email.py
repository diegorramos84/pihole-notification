from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email_sender = 'fendeorc@gmail.com'
email_password = os.getenv('EMAIL_PASSWORD')

email_receiver = 'diegorramos84@gmail.com'

subject = 'Pi Hole is not working properly'
body = """
Pi Hole is not working properly
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())