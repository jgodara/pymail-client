# Pymail Client

A mailbox that can connect to your IMAP server, fetch emails and index them locally.

## Installation/Running instructions

You need to have Python3 `pipenv` and `npm` installed.

```shell
pip3 install pipenv
git clone https://github.com/jgodara/pymail-client.git
cd pymail-client
npm i
```

Enter the pipenv shell and install all dependencies by

```shell
pipenv shell
pipenv install
```

Run the server

```shell
python mailbox.py
```

## TODOs

1. Make email reading async
1. Make sidebar labels/folders dynamic
1. Make emails go to the index
1. Figure out a way to read email content
1. AND ALL OTHER IMPORTANT MAILBOX FEATURES (oof)
