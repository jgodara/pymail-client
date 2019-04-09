from sqlite_orm.table import BaseTable
from sqlite_orm.field import IntegerField, TextField, BooleanField


class Email(BaseTable):
    __table_name__ = 'emails'

    id = IntegerField(primary_key=True, auto_increment=True)
    subject = TextField()
    content = TextField()
    from_addr = TextField()
    to_addr = TextField()
    cc_addr = TextField()
    has_attachment = BooleanField()
    read = BooleanField()
    starred = BooleanField()


class Settings(BaseTable):
    __table_name__ = 'settings'

    id = IntegerField(primary_key=True, auto_increment=True)
    email_address = TextField(not_null=True)
    user_password = TextField(not_null=True)
    imap_server_url = TextField(not_null=True)
    master_password = TextField(not_null=True)
