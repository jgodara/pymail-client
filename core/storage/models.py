from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation

Base = declarative_base()


class Settings(Base):
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_password = Column(String, nullable=False)
    imap_server_url = Column(String, nullable=False)
    master_password = Column(String, nullable=False)


class Email(Base):
    __tablename__ = 'emails'

    id = Column(String, primary_key=True)
    subject = Column(String)
    received_date = Column(String)
    content = Column(String)
    from_addr = Column(String)
    to_addr = Column(String)
    cc_addr = Column(String)
    has_attachment = Column(Boolean, default=False)
    read = Column(Boolean, default=False)
    starred = Column(Boolean, default=False)

    setting_id = Column(Integer, ForeignKey("settings.id"), nullable=False)
    setting = relation(Settings)
