from flask import Flask
from flask_restful import Api

from api.resources.emails import Emails
from api.resources.settings import Settings

app = Flask(__name__, static_folder="frontend", static_url_path="/frontend")
api = Api(app)


@app.route('/')
def root_controller():
    return app.send_static_file('src/index.html')


api.add_resource(Settings, '/api/settings')
api.add_resource(Emails, '/api/emails')

if __name__ == '__main__':
    app.run(port=8080)

