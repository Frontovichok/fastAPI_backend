from sqlalchemy import Column, Integer, String, ARRAY, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base
from sqlalchemy.dialects.postgresql import JSONB


class Static_analysis(Base):
    __tablename__ = 'static_analysis'

    id = Column(Integer, primary_key=True, index=True)
    # связать с проектом
    # project_id = Column(Integer, ForeignKey('projects.id'), unique=True)
    project_id = Column(Integer, ForeignKey('projects.id'), unique=True)
    build_status = Column(String)
    binaries_status = Column(String)
    extra_files_status = Column(String)
    extra_functions_status = Column(String)
    vulnerabilities_status = Column(String)
    programming_languages = Column(ARRAY(String))
    # коллекция, которая хранит в себе связь с таблицей Binary_search_history
    # в ней хранятся все строки таблицы Binary_search_history, имеющие отношение с таблицей Static_analysis
    # binary_search_history = relationship(
    #     'Binary_search_history', backref='static_analysis')

    # binary_search_history = relationship(
    #     "Binary_search_history", backref="static_analysis")

    # projects = relationship('Projects', back_populates='static_analysis')


class Binary_search_history(Base):
    __tablename__ = 'binary_search_history'

    id = Column(Integer, primary_key=True, index=True)
    # связать с проектом
    project_id = Column(Integer, ForeignKey(
        'static_analysis.project_id'))

    # project_id = Column(Integer)

    path_to_source_directory = Column(String)
    status = Column(String)
    time = Column(DateTime)
    # результат анализа - JSON файл со списком бинраных файлов с указанием их местонахождения
    result = Column(String)
    static_analysis = relationship(
        "Static_analysis", backref="binary_search_history")


class Extra_files_search_history(Base):
    __tablename__ = 'extra_files_search_history'

    id = Column(Integer, primary_key=True, index=True)
    # связать с проектом
    project_id = Column(Integer)
    path_to_source_directory = Column(String)
    status = Column(String)
    time = Column(DateTime)
    # результат анализа - JSON файл со списком избыточных файлов с указанием их местонахождения
    result = Column(JSONB)


class Extra_functions_search_history(Base):
    __tablename__ = 'extra_functions_search_history'

    id = Column(Integer, primary_key=True, index=True)
    # связать с проектом
    project_id = Column(Integer)
    path_to_source_directory = Column(String)
    status = Column(String)
    time = Column(DateTime)
    # результат анализа - JSON файл со списком избыточных функций с указанием их местонахождения
    result = Column(JSONB)


class Vulnerabilities_analyze_history(Base):
    __tablename__ = 'vulnerabilities_analyze_history'

    id = Column(Integer, primary_key=True, index=True)
    # связать с проектом
    project_id = Column(Integer)
    path_to_source_directory = Column(String)
    status = Column(String)
    time = Column(DateTime)
    # результат анализа - JSON файл со списком уязвимостей и их обоснованиями
    result = Column(JSONB)
