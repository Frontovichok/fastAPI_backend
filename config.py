from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:4444@localhost:5432/python_db"

# создает новый экземпляр класса sqlalchemy.engine.Engine который предоставляет подключение к базе данных
engine = create_engine(DATABASE_URL)

# sessionmaker - фабрика для создания сессий с заданными параметрами, вместо задания сессий по одной
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех моделей, от которого они наследуются
# С помощью разных базовых классов можно организовать подключение к разным базам данных
Base = declarative_base()