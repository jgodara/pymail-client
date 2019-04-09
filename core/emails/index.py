import email
import imaplib
import random

import cryptutils
from core.storage.database_utils import initialize_database, database
from core.storage.models import Email, Settings


def create_email(email_row) -> Email:
    email = Email()

    email.id = email_row[0]
    email.subject = email_row[1]
    email.content = email_row[2]
    email.from_addr = email_row[3]
    email.to_addr = email_row[4]
    email.cc_addr = email_row[5]
    email.has_attachment = email_row[6]
    email.read = email_row[7]
    email.starred = email_row[8]

    return email


class EmailIndex:
    __instance = None

    emails: [Email] = []

    @staticmethod
    def get_instance():
        if EmailIndex.__instance is None:
            EmailIndex()

        return EmailIndex.__instance

    def __init__(self):
        if EmailIndex.__instance is None:
            initialize_database("mailbox", [Email])
            with database("mailbox") as db:
                for email in db.query(Email).select().execute():
                    self.emails.append(create_email(email))
            EmailIndex.__instance = self

            self.process_emails()

    def get_emails(self) -> [Email]:
        return self.emails

    def process_emails(self):
        with database("settings") as db:
            for row in db.query(Settings).select().execute():
                email_address = cryptutils.decodestr(row[1])
                email_password = cryptutils.decodestr(row[2])
                imap_url = cryptutils.decodestr(row[3])

                im = imaplib.IMAP4_SSL(imap_url)
                try:
                    rv, data = im.login(email_address, email_password)
                except imaplib.IMAP4.error as err:
                    print("Login Failed", err)
                    exit(1)

                im.select("Inbox")

                _, data = im.search(None, "ALL")

                for num in data[0].split():
                    _, data = im.fetch(num, "(RFC822)")

                    if num.decode("utf-8") == "5":
                        break

                    message = email.message_from_bytes(data[0][1])
                    header = email.header.make_header(email.header.decode_header(message["Subject"]))

                    subject = str(header)

                    email_model = Email()
                    email_model.subject = subject
                    # email_model.content = message._payload[0]

                    email_model.id = random.randint(100, 10000)

                    self.emails.append(email_model)
