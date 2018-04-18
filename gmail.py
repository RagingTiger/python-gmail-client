#!/usr/bin/env python

"""
author: tigerj
references: https://stackoverflow.com/a/24364538 Ricky Wilson 6/23/14
usage: python gmail.py subject body
"""

# libs
import os
import sys
import smtplib


# classes
class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()

        # upggrade to secure
        session.starttls()
        session.ehlo()
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, body):
        ''' Format and send email to smtp.gmail.com relay '''
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
            "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            self.email,
            headers + "\r\n\r\n" + body)


# executable
if __name__ == '__main__':

    # get env vars
    try:
        gmail_creds = {'account': os.environ['GMAIL_ACCOUNT'],
                       'psswd': os.environ['GMAIL_APP_PSSWD']}
    except KeyError:
        sys.exit('Please check shell environment variables are set and try '
                 'again. ref: '
                 'https://en.wikipedia.org/wiki/Environment_variable')

    # start gmail SMTP session
    gm = Gmail(gmail_creds['account'], gmail_creds['psswd'])

    # get message subject and body from command line args
    try:
        message = {'subject': str(sys.argv[1]), 'body': str(sys.argv[2])}
    except IndexError:
        sys.exit('Usage: python gmail.py subject body')

    # send mesage
    gm.send_message(message['subject'], message['body'])
