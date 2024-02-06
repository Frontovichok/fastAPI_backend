# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# DATABASE_URL = "postgresql://postgres:4444@localhost:5432/python_db"

# # создает новый экземпляр класса sqlalchemy.engine.Engine который предоставляет подключение к базе данных
# engine = create_engine(DATABASE_URL)

# # sessionmaker - фабрика для создания сессий с заданными параметрами, вместо задания сессий по одной
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Базовый класс для всех моделей, от которого они наследуются
# # С помощью разных базовых классов можно организовать подключение к разным базам данных
# Base = declarative_base()

# Загружаем переменные из файла .env
load_dotenv()

# Получаем необходимые переменные из загруженных переменных файла .env
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")