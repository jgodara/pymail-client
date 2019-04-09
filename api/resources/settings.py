from flask_restful import Resource, reqparse

from core.settings.user_settings import UserSettings

from core.storage.models import Settings as SettingsModel

parser = reqparse.RequestParser()
parser.add_argument("email_address")
parser.add_argument("user_password")
parser.add_argument("imap_server_url")
parser.add_argument("master_password")


class Settings(Resource):
    has_error = False
    error_code = None

    settings_object = None

    def __init__(self):
        user_settings = UserSettings().get_user_settings()
        if user_settings is None:
            self.has_error = True
            self.error_code = "NO_MASTER_PASS"
        else:
            settings = {
                "email_address": user_settings[1],
                "user_password": user_settings[2],
                "imap_server_url": user_settings[3],
                "master_password": user_settings[4]
            }
            self.settings_object = settings

    def get(self):
        if not self.has_error:
            return {"settings": self.settings_object}

        return {"success": False, "code": self.error_code}, 403

    def post(self):
        kwargs = {}
        args = parser.parse_args()
        for key in args:
            value = args[key]
            if value is not None:
                kwargs[key] = value

        UserSettings().update_user_settings(**kwargs)

    def get_settings(self) -> SettingsModel:
        settings = SettingsModel()
        settings.master_password = self.settings_object["master_password"]
        settings.imap_server_url = self.settings_object["imap_server_url"]
        settings.user_password = self.settings_object["user_password"]
        settings.email_address = self.settings_object["email_address"]

        return settings
