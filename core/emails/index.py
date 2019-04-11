import email
import imaplib
import random
from threading import Thread

import cryptutils
from core.storage.models import Email, Settings
from core.storage.database import session as db


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
            EmailIndex.__instance = self

            email_index_thread = Thread(target=self.process_emails)
            email_index_thread.start()

    def get_emails(self) -> [Email]:
        return self.emails

    def process_emails(self):
        settings = db.query(Settings).filter(Settings.id == 1)
        if settings is None:
            return

        email_address = cryptutils.decodestr(settings.email_address)
        email_password = cryptutils.decodestr(settings.email_password)
        imap_url = cryptutils.decodestr(settings.imap_url)

        im = imaplib.IMAP4_SSL(imap_url)
        try:
            im.login(email_address, email_password)
        except imaplib.IMAP4.error as err:
            print("Login Failed", err)
            exit(1)

        im.select("Inbox")

        _, data = im.search(None, "ALL")

        for num in data[0].split():
            _, data = im.fetch(num, "(RFC822)")

            message = email.message_from_bytes(data[0][1])
            header = email.header.make_header(email.header.decode_header(message["Subject"]))

            subject = str(header)

            email_model = Email()
            email_model.subject = subject
            # TODO Email bodies
            # email_model.content = message._payload[0]

            email_model.id = random.randint(100, 10000)

            self.emails.append(email_model)
