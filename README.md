🔧 Sharing a recent experience with my Raspberry Pi setup! 🍓🔌 I noticed the other day that my Pi-hole had crashed without me even realizing it – yikes! 🚫⚡ To prevent such downtime in the future, I decided to create a quick notification script because, let's face it, constant uptime is the goal!

First, I crafted a Python script to keep an eye on the Pi-hole status and take action if it's disabled:

```python
import subprocess

pihole_status = subprocess.getoutput("pihole status")

if "enabled" not in pihole_status:
    subprocess.run(["python", "send_email.py"])
    print('Pi-hole is not running properly. Status:', pihole_status)
```

Next, I whipped up a Python email script. A helpful YouTube tutorial (https://www.youtube.com/watch?v=g_j6ILT-X0k) guided me through the process:

```python
from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = 'sender_email@gmail.com'
email_password = os.getenv('EMAIL_PASSWORD')
receiver_email = 'receiver_email@gmail.com'
# ... other email setup ...

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, email_password)
    smtp.sendmail(sender_email, receiver_email, em.as_string())
```

Please note: To send email with Python, you'll need to follow this guide to allow less secure apps: https://support.google.com/accounts/answer/185833?hl=en 📧🔒

Lastly, I automated the process by adding a task to crontab, scheduling the script to run every day at 8 am:

```bash
crontab -e

# Add the following line, replacing path to the correct file path
0 8 * * * /usr/bin/python /path/to/pihole_status_check.py
```

This `0 8 * * *` schedule means the script runs at 8:00 AM every day.⏰

I'm all about optimizing my Raspberry Pi setup! 🛠️ Stay tuned for more tech adventures and solutions! 🚀🔧 #RaspberryPi #Automation #TechHacks #Programming #LinkedInTech
