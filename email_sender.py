#!/usr/bin/env python3

import smtplib

from email.message import EmailMessage


def emailutility(messageBody):
    msg = EmailMessage()

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'TEST email'
    msg['From'] = 'ravi_chappa@uhc.com'
    msg['To'] = 'ravi_chappa@uhc.com'
    msg.set_content(messageBody)

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('mailo2.uhc.com')
    s.send_message(msg)
    s.quit()
