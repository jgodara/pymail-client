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
        emails = []

        for i in range(10):
            email = Email()
            email.id = i
            email.from_addr = f"Himanshu {i}"
            email.subject = f"Email Subject {i}"
            email.has_attachment = True if i % 3 is 0 else False
            email.read = True if i % 2 is 0 else False
            email.starred = True if i % 5 is 0 else False

            emails.append(email)

        return emails
