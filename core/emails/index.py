import email
import imaplib

import cryptutils
from core.storage.database import SessionFactoryPool
from core.storage.models import Email, Settings


def process_emails():
    """
    Thread that runs forever to read and index emails from the remote IMAP
    server.
    """
    # Same database session cannot be used across multiple threads
    session = SessionFactoryPool.create_new_session()
    settings = session.query(Settings).filter(Settings.id == 1).first()

    # Don't do anything if no email account is configured
    # SEE https://github.com/jgodara/pymail-client for config instructions
    if settings is None:
        return

    # Load basic IMAP account configuration
    email_address = cryptutils.decodestr(settings.email_address)
    email_password = cryptutils.decodestr(settings.user_password)

    # Log into the remote IMAP Server
    imap_login = imaplib.IMAP4_SSL(
        cryptutils.decodestr(settings.imap_server_url))
    try:
        imap_login.login(email_address, email_password)
    except imaplib.IMAP4.error as err:
        print("Login Failed", err)
        exit(1)

    # TODO Read all folders
    imap_login.select("Inbox")

    _, data = imap_login.search(None, "ALL")

    for num in data[0].split():
        _, data = imap_login.fetch(num, "(RFC822)")

        message = email.message_from_bytes(data[0][1])
        message_headers = dict()
        for key in message:
            header = email.header.decode_header(message[key])
            header_value = email.header.make_header(header)

            message_headers[key.lower()] = str(header_value)

        message_id = message_headers["message-id"]
        email_model = session.query(Email).filter(
            Email.id == message_id).first()
        if email_model is None:
            email_model = Email()
            email_model.id = message_id
            email_model.subject = message_headers["subject"]
            email_model.received_date = message_headers["date"]
            email_model.to_addr = message_headers["to"]
            email_model.from_addr = message_headers["from"]
            email_model.setting = settings
            # TODO Email bodies
            # email_model.content = message._payload[0]

            try:
                session.add(email_model)
                session.commit()
            except:
                session.rollback()

    # Close the session
    session.close()


class EmailIndex:
    __instance = None

    @staticmethod
    def get_instance():
        if EmailIndex.__instance is None:
            EmailIndex()

        return EmailIndex.__instance

    def __init__(self):
        if EmailIndex.__instance is None:
            EmailIndex.__instance = self

    def get_emails(self) -> [Email]:
        return SessionFactoryPool.get_current_session().query(Email).all()
