from sqlite_orm.table import BaseTable
from sqlite_orm.field import IntegerField, TextField


class Email(BaseTable):
    __table_name__ = 'emails'

    id = IntegerField(primary_key=True, auto_increment=True)
    subject = TextField
    content = TextField


class Settings(BaseTable):
    __table_name__ = 'settings'

    id = IntegerField(primary_key=True, auto_increment=True)
    email_address = TextField
    user_password = TextField
    imap_server_url = TextField
    master_password = TextField
