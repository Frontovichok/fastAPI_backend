from datetime import datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# from sqlalchemy.ext.declarative import declarative_base

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from models.auth_models import role

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# Base = declarative_base()


# Базовый класс для всех моделей. Обычно его называют Base, и все модели приложения наследуют от этого класса.
# Этот declarative base class содержит справочник всех «своих» таблиц и соответствующих ему классов.
# Обычно Base один на приложение, его заводят в общем модуле.
class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


# Соединение SQLAlchemy с базой данных
engine = create_async_engine(DATABASE_URL)
# Создаем сессии подключения к БД (временные соединения) для взаимодействия с БД (обновить, удалить, создать ...)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# Получить сессию асинхронно
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


# Получение пользователя (со всеми параметрами функции get_async_session)
async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
