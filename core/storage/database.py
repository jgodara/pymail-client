from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import utils

import constants
from core.storage.models import Base as DeclarativeBase

sqlite_file = f"sqlite:///{constants.work_dir}/pymail.db"
utils.create_file_if_needed(sqlite_file)

database_engine = create_engine(sqlite_file)
DeclarativeBase.metadata.create_all(database_engine)
DeclarativeBase.bind = database_engine

session = sessionmaker()
session.configure(bind=database_engine)
session = session()
