from flask_restful import Resource

from core.emails.index import EmailIndex


class Emails(Resource):
    def get(self):
        response = {"emails": []}
        email_index = EmailIndex.get_instance()

        for email in email_index.get_emails():
            response["emails"].append({"subject": email.subject, "content": email.content})

        return response
