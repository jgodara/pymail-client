import core.storage.database_utils as db_utils
from core.storage.models import Settings


class UserSettings:
    user_settings = None

    def __init__(self):
        db_utils.initialize_database("settings", [Settings])
        with db_utils.database("settings") as db:
            for settings in db.query(Settings).select().execute():
                self.user_settings = settings

    def get_user_settings(self):
        return self.user_settings
