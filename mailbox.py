from threading import Thread

from flask import Flask
from flask_restful import Api

from api.resources.emails import Emails
from api.resources.settings import Settings
from core.emails.index import process_emails

app = Flask(__name__, static_folder="frontend", static_url_path="/frontend")
api = Api(app)


@app.route('/')
def root_controller():
    """
    Root Controller: Renders the React front-end
    :return: The index.html page containing the React front
    """
    return app.send_static_file('src/index.html')


api.add_resource(Settings, '/api/settings')
api.add_resource(Emails, '/api/emails')

if __name__ == '__main__':
    # Start the email indexing thread
    email_index_thread = Thread(target=process_emails)
    email_index_thread.start()

    # Bind only locally for security
    app.run(port=8080, host="127.0.0.1")
