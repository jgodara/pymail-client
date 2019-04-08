from flask_restful import Resource

from core.settings.user_settings import UserSettings


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
            self.settings_object = user_settings

    def get(self):
        if not self.has_error:
            return {"settings": self.settings_object}

        return {"success": False, "code": self.error_code}
