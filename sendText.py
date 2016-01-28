#!/usr/bin/python

import smtplib

print "setting up smtp lib gmail server"

server = smtplib.SMTP( 'smtp.gmail.com' )

print "starting tls"
server.starttls()

print "logging in to server"
server.login( 'craighomealarm', '1280Ithaca' )

print "sending sms"
server.sendmail( 'craighomealarm', '7202734478@mms.att.net', 'TEsT' )
print "done"
