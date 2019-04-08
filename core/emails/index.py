from core.storage.models import Email
from core.storage.database_utils import initialize_database


class EmailIndex:
    __instance = None

    @staticmethod
    def get_instance():
        if EmailIndex.__instance is None:
            EmailIndex()

        return EmailIndex.__instance

    def __init__(self):
        if EmailIndex.__instance is None:
            initialize_database("mailbox", [Email])
            EmailIndex.__instance = self

    def get_emails(self):
        email = Email()
        email.subject = "Dummy"
        email.content = "Dummy"

        emails = [email]

        return emails
