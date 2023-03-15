# Создаем Модели
# Модель - класс Python, соответствующий таблице в БД, а его свойства - таблицы

from sqlalchemy import Column, Integer, String
from config import Base

class Book(Base):
  __tablename__ = 'book'

  # к типу Integer автоматически добавляется свойство autoincrement=True
  id=Column(Integer, primary_key=True, index=True)
  title=Column(String)
  description=Column(String)

class Accounts(Base):
  __tablename__ = 'accounts'


  id=Column(Integer, primary_key=True, index=True)
  firstname=Column(String)
  surname=Column(String)
  patronymic=Column(String)