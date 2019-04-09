import core.storage.database_utils as db_utils
from core.storage.models import Settings


class UserSettings:
    __database_name = "settings"

    user_settings = None

    def __init__(self):
        db_utils.initialize_database(self.__database_name, [Settings])
        with db_utils.database(self.__database_name) as db:
            for settings in db.query(Settings).select().execute():
                self.user_settings = settings

    def get_user_settings(self):
        return self.user_settings

    def update_user_settings(self, **kwargs):
        for key in kwargs:
            print(key)
        with db_utils.database(self.__database_name) as db:
            if self.user_settings is None:
                settings = Settings()
                for key in kwargs:
                    settings.__setattr__(key, kwargs[key])

                settings.id = 1
                db.query(Settings).insert(settings).execute()
            else:
                db.query(Settings).update(**kwargs).execute()
