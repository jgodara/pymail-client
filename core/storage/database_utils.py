import errno
from sqlite_orm.database import Database

import os

from sqlite_orm.exception import OperationalError

import constants


def initialize_database(db_name, models):
    with database(db_name) as db:
        for model in models:
            try:
                db.query(model).create().execute()
            except OperationalError:
                # Ignore if table exists
                pass


def database(db_name):
    database_path = f"{constants.work_dir}/{db_name}.db"
    create_file_if_needed(database_path)
    return Database(database_path)


def create_file_if_needed(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as ex:
            if ex.errno != errno.EEXIST:
                raise
