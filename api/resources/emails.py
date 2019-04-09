from flask_restful import Resource

from core.emails.index import EmailIndex


class Emails(Resource):
    email_index = None
    name = None

    def __init__(self):
        self.email_index = EmailIndex.get_instance()

    def get(self):
        response = {"emails": []}

        for email in self.email_index.get_emails():
            response["emails"].append({
                "id": email.id,
                "subject": email.subject,
                "content": email.content,
                "from": email.from_addr,
                "time": "9:27 AM",
                "hasAttachment": email.has_attachment,
                "read": email.read,
                "starred": email.starred
            })

        return response

    def post(self):
        pass
