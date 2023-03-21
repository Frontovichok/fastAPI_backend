from sqlalchemy import Column, Integer, String, ARRAY, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    post = Column(String)
    gender = Column(String)
    cabinet = Column(String)
    phone_number_work = Column(String)
    phone_number_mobile = Column(String, unique=True, nullable=False)
    email = Column(String)
    status = Column(String)
    access_level = Column(String)
    working_from = Column(DateTime)

    # Нужно для будущей авторизации
    login = Column(String, unique=True, nullable=False)
    password_hash = Column(String, unique=True, nullable=False)
