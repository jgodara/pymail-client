from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Email(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    subject = Column(String)
    content = Column(String)
    from_addr = Column(String)
    to_addr = Column(String)
    cc_addr = Column(String)
    has_attachment = Column(Boolean, default=False)
    read = Column(Boolean, default=False)
    starred = Column(Boolean, default=False)


class Settings(Base):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_password = Column(String, nullable=False)
    imap_server_url = Column(String, nullable=False)
    master_password = Column(String, nullable=False)
