![GitHub](https://img.shields.io/github/license/jgodara/pymail-client.svg?color=RED&label=License&style=for-the-badge)

# Pymail Client

A mailbox that can connect to your IMAP server, fetch emails and index them locally.

## Installation/Running instructions
You need to have Python3 `pipenv` and `npm` installed.

```bash
pip3 install pipenv
git clone https://github.com/jgodara/pymail-client.git
cd pymail-client
npm i
```

Enter the pipenv shell and install all dependencies by

```bash
pipenv shell
pipenv install
```

Run the server

```bash
python mailbox.py
```

Configure Pymail Client to use your email (IMAP)

```bash
curl -X POST 'http://localhost:8080/api/settings' \
 -d 'email_address=<youremail>&user_password=<yourpassword>&imap_server_url=<yoururl>&master_password=abcd'
```

## TODOs

1. Make email reading async
1. Make sidebar labels/folders dynamic
1. Make emails go to the index
1. Figure out a way to read email content
1. AND ALL OTHER IMPORTANT MAILBOX FEATURES (oof)
