#/usr/bin/env python

import smtplib

def sendText():
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login("craighomealarm@gmail.com", "1280Ithaca")
    server.sendmail('craighomealarm', '7202734478@mms.att.net', 'Home Alarm has been triggered!!')

sendText()
