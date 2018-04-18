## About
A simple *Python class* (Python 2) and CLI to wrap the sending of emails
programmatically from *Python* using *Gmail's smtp relay* (i.e. smtp.gmail.com).

## Download Source
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

## Setup
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
