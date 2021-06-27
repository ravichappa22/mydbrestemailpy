#!/usr/bin/env python3

import smtplib
import os

from email.message import EmailMessage


def emailutility(messageBody):
    msg = EmailMessage()

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'TEST SCR'
    msg['From'] = os.getenv("EMAIL_FROM")
    msg['To'] = os.getenv("EMAIL_TO")
    msg.set_content(messageBody)

    # Send the message via our own SMTP server.
    s = smtplib.SMTP(os.getenv("SMTP_HOST"))
    s.send_message(msg)
    print("email sent successfully")
    s.quit()
