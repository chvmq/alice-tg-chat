from sqlalchemy import Column, Integer, String, Boolean

from .base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = Column(String, unique=True)
    telegram_id = Column(String, unique=True)
    chat_id = Column(String, unique=True)

    #Added with migration
    is_chatting = Column(Boolean)
