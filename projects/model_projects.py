from sqlalchemy import Column, Integer, String, ARRAY, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base


class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    account_id = Column(Integer)
    # authors = relationship("Account", secondary="")
    name = Column(String)
    company = Column(String)
    sertification_type = Column(String)
    trust_level = Column(String)
    number = Column(String)
    # Привязать к аккаунтам, экспертов может быть несколько
    experts = Column(String)
    solution = Column(String)
    source_directory = Column(String)
    distrib_directory = Column(String)
    documentation_directory = Column(String)
    status = Column(String)
    reports_directory = Column(String)
    # создать связь с работой(полями этой же таблицы), подпроектом которого является данный компонент
    main_component = Column(String)
    # создать связь с компонентами(полями этой же таблицы), которые входят в данную работу
    subcomponents = Column(String)
