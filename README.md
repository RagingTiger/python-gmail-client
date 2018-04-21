## About
A simple *Python class* (for both Python 2 and Python 3) and CLI to wrap the sending of emails
programmatically from *Python* using *Gmail's smtp relay* (i.e. smtp.gmail.com).

## Download Source
Instead of *cloning* the entire repo, you can download the python source
straight to your project directory, and import it directly into your project.
First set the version you want to either `python2` or `python3` as follows:
```
PYVERS=python2
```
or
```
PYVERS=python3
```
Then download using curl:
```
curl -o gmail.py https://raw.githubusercontent.com/RagingTiger/python-gmail-client/$PYVERS/gmail.py
```
or download using wget:
```
wget https://raw.githubusercontent.com/RagingTiger/python-gmail-client/$PYVERS/gmail.py
```

## Setup Gmail SMTP Relay
### 1: Create Gmail Account
To use this, you will need to setup a *Gmail* account. This should be rather facile. Click the below link to setup your account:

https://support.google.com/mail/answer/56256?hl=en

### 2: Turn on 2-Step Verification
The next step will be to activate *2-Step Verification*. This will be key to
creating an *App Password* later. Click the below link and follow the   
instructions:

https://support.google.com/accounts/answer/185839


### 3: Generate App Password
Now with your newly created *Gmail* account, you will want to setup an *App
Password*. This will allow your app, and the *Gmail* python class, to access
your *Gmail* account as an *smtp relay* and forward email. Click the below
link to setup your *App Password*:

https://support.google.com/accounts/answer/185833?hl=en

First click where it says *"How to generate an App password"*, and click *"App
passwords"*:

<p align="center">
  <img src="https://raw.githubusercontent.com/RagingTiger/python-gmail-client/master/assets/images/app_psswd1.png"/>
</p>

Then click *"Select app"*, select *"Other"*, and give your app a name (e.g.
MyWebApp):

<p align="center">
  <img
  src="https://raw.githubusercontent.com/RagingTiger/python-gmail-client/master/assets/images/app_psswd2.png"/>
</p>

Finally, the *"App Password"* is generated:

<p align="center">
  <img
  src="https://raw.githubusercontent.com/RagingTiger/python-gmail-client/master/assets/images/app_psswd3.png"/>
</p>

## How to Access Credentials
Now that you have both a **Gmail account** and **App password**, how do you use them with the `gmail.py` module? One way is to use [environment variables](https://en.wikipedia.org/wiki/Environment_variable). The `executable` section of the `gmail.py` module only works with "environment variables". Specifically it looks for a variable called `GMAIL_ACCOUNT` and a variable called `GMAIL_APP_PSSWD`:
```
.
.
.
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
  .
  .
  .
```
While the module has been implemented without any *"hard-coded"* way to load the `account` and `passwd` information, the above implementation with environment variables is a well known solution. **DISCLAIMER:** *Do not* put your **Gmail account** or **App Password** directly into your source code.

A simple implementation of an email client using the `gmail.py` module could
look like the following:
```
$ # from your $SHELL
$ export GMAIL_ACCOUNT=username@gmail.com
$ export GMAIL_APP_PSSWD=password

# then write the script as follows
$ nano emailclient.py

  # libs
  import os
  import gmail

  # get credentials
  gmail_creds = {'account': os.environ['GMAIL_ACCOUNT'],
                 'psswd': os.environ['GMAIL_APP_PSSWD']}

  # start gmail SMTP session
  gm = gmail.Gmail(gmail_creds['account'], gmail_creds['psswd'])

  # send message
  gm.send_message('This is the subject', 'This is the body')

# then run your program
$ python emailclient.py
```
