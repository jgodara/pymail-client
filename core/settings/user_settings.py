from core.storage.models import Settings
from core.storage.database import SessionFactoryPool


class UserSettings:
    __database_name = "settings"

    user_settings: Settings = None
    session = None

    def __init__(self):
        self.session = SessionFactoryPool.get_current_session()

    def get_user_settings(self):
        return self.session.query(Settings).filter(Settings.id == 1).first()

    def update_user_settings(self, **kwargs):
        settings = self.user_settings
        perform_create = False

        if settings is None:
            settings = Settings()
            settings.id = 1

            perform_create = True
        for key in kwargs:
            value = kwargs[key]
            if value:
                settings.__setattr__(key, value)

        if perform_create:
            self.session.add(settings)

        self.session.commit()
