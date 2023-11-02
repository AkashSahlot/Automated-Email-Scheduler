import os
import random
import datetime
import ssl # internet secure connectionn and safeguarding
from email.message import EmailMessage
import smtplib

email_sender='yashakash.singh7@gmail.com'
email_password='**** **** **** ****'          #os.environ.get("EMAIL_PASSWORD")
email_receiver=['akash.singh9@delhivery.com'] # receiver address

subject='Greeting Mail'

good_morning_wish=["Good Morning",
                   "Wishing you a bright and cheerful morning!",
                   "Rise and shine!",
                   "Sending you positive vibes for a great day ahead!",
                   "May your day be filled with joy and positivity!"]


good_night_wish=["Good night, Wishing you a restful sleep and a productive day tomorrow!",
    "Wishing you a peaceful night's rest",
    "Good night, May you wake up refreshed and ready to conquer the day!",
    "Sending you my best wishes for a good night's sleep",
    "Have a restful night, Tomorrow is a new day full of opportunities!",
    "Wishing you sweet dreams and a rejuvenating night",
    "Good night, Take some time to relax and recharge.",
    "May you have a peaceful night's sleep and wake up with renewed energy",
    "Wishing you a good night's rest and a successful day ahead",
    "Sleep well, Tomorrow holds great promise!",]


body1=random.choice(good_morning_wish)
body2=random.choice(good_night_wish)
em=EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body2)


context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())
except Exception as e:
    print('Error:',e)
