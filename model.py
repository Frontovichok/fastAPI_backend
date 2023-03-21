# Создаем Модели
# Модель - класс Python, соответствующий таблице в БД, а его свойства - таблицы

from sqlalchemy import Column, Integer, String, ARRAY, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config import Base
from sqlalchemy.dialects.postgresql import JSONB

class Book(Base):
    __tablename__ = 'book'

    # к типу Integer автоматически добавляется свойство autoincrement=True
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)





# Одна таблица с проектами и компонентами,
# если это главное изделие, то заполняется столбец subcomponents, в котором указаны id компонетов (связать с другими полями этой таблицы)
# если это компонент, который входит в главное изделие, то заполняется столбец main_component, в котором указывается id главного изделия (связать с другим полем этой таблицы)
# необходимо создать связь многие ко многим, чтобы у каждого аккаунта был список проектов, которые к нему привязаны:
# https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy
# https://www.gormanalysis.com/blog/many-to-many-relationships-in-fastapi/
class Projects(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, primary_key=True, index=True)
    # authors = relationship("Account", secondary="")
    name = Column(String)
    company = Column(String)
    sertification_type = Column(String)
    trust_level = Column(String)
    number = Column(String)
    # Привязать к аккаунтам, экспертов может быть несколько
    experts = Column(ARRAY(Integer))
    solution = Column(Integer)
    source_directory = Column(String)
    distrib_directory = Column(String)
    documentation_directory = Column(String)
    status = Column(String)
    reports_directory = Column(String)
    # создать связь с работой(полями этой же таблицы), подпроектом которого является данный компонент
    main_component = Column(String)
    # создать связь с компонентами(полями этой же таблицы), которые входят в данную работу
    subcomponents = Column(ARRAY(String))

    static_analysis = relationship(
        'Static_analysis', backref='projects')

# подумать нужна ли эта таблица, которая будет аккумулировать данные из других таблиц, которые содержат данные из программной документации


# ----------------------------------------------------------------------Documentation analysis---------------------------------------------------------

class Documentation(Base):
    __tablename__ = 'documentation'

    id = Column(Integer, primary_key=True, index=True)

    # привязать внешние ключи: id проекта
    # id_project=Column(Integer)


class Specification(Base):
    __tablename__ = 'specification'

    id = Column(Integer, primary_key=True, index=True)
    # создать связь с работой, для которой имеется данная спецификация
    id_project = Column(Integer)
    trust_level = Column(Integer, default=4)
    # https://amercader.net/blog/beware-of-json-fields-in-sqlalchemy/
    # exaple JSONB:
    # [
    #     {
    #         "alright": True,
    #         "requirement": "Сведение о составе ПО",
    #         "expert_comment": "Необходимые сведения присутствуют"
    #     },
    #     {
    #         "alright": False,
    #         "requirement": "Сведение о документации на ПО",
    #         "expert_comment": "Необходимые сведения отсутствуют"
    #     }
    # ]
    requirements = Column(JSONB)


class Program_description(Base):
    __tablename__ = 'program_description'

    id = Column(Integer, primary_key=True, index=True)
    # создать связь с работой, для которой имеется Описание программы
    id_project = Column(Integer)
    trust_level = Column(Integer, default=4)
    # https://amercader.net/blog/beware-of-json-fields-in-sqlalchemy/
    # exaple JSONB:
    # [
    #     {
    #         "alright": True,
    #         "requirement": "Сведение о составе ПО",
    #         "expert_comment": "Необходимые сведения присутствуют"
    #     },
    #     {
    #         "alright": False,
    #         "requirement": "Сведения о среде функционирования",
    #         "expert_comment": "Необходимые сведения отсутствуют"
    #     },
    #     {
    #         "alright": True,
    #         "requirement": "Сведения о среде функционирования",
    #         "expert_comment": "Необходимые сведения отсутствуют"
    #     }
    # ]
    requirements = Column(JSONB)


class Use_description(Base):
    __tablename__ = 'use_description'

    id = Column(Integer, primary_key=True, index=True)
    # создать связь с работой, для которой имеется Описание программы
    id_project = Column(Integer)
    trust_level = Column(Integer, default=4)
    # https://amercader.net/blog/beware-of-json-fields-in-sqlalchemy/
    # exaple JSONB:
    # [
    #     {
    #         "alright": True,
    #         "requirement": "Сведение об области применения ПО",
    #         "expert_comment": "Необходимые сведения присутствуют"
    #     },
    #     {
    #         "alright": False,
    #         "requirement": "Сведения о ограничениях при применении",
    #         "expert_comment": "Необходимые сведения отсутствуют"
    #     },
    #     {
    #         "alright": True,
    #         "requirement": "Сведения о минимальной конфигурации",
    #         "expert_comment": "Необходимые сведения отсутствуют"
    #     }
    # ]
    requirements = Column(JSONB)


class Explonatory_note(Base):
    __tablename__ = 'explonatory_note'

    id = Column(Integer, primary_key=True, index=True)
    # создать связь с работой, для которой имеется Описание программы
    id_project = Column(Integer)
    trust_level = Column(Integer, default=3)
    # https://amercader.net/blog/beware-of-json-fields-in-sqlalchemy/
    # exaple JSONB:
    # [
    #     {
    #         "alright": True,
    #         "requirement": "Сведение о назначении компонентов",
    #         "expert_comment": "Необходимые сведения присутствуют"
    #     },
    #     {
    #         "alright": False,
    #         "requirement": "Сведения о праментрах обрабатываемых наборов данных",
    #         "expert_comment": "Необходимые сведения отсутствуют"
    #     },
    #     {
    #         "alright": True,
    #         "requirement": "Сведения об алгоритмах функционирования ПО",
    #         "expert_comment": "Необходимые сведения отсутствуют"
    #     }
    # ]
    requirements = Column(JSONB)

# Пока только самые базовые данные, в дальнейшем будет модифицироваться, чтобы можно было считать КС в данной программе


class Checksum(Base):
    __tablename__ = 'checksum'

    id = Column(Integer, primary_key=True, index=True)
    # связать с проектом
    id_project = Column(Integer)
    # путь к каталогу, в которм хранятся все файлы с контрольным суммированием иходников, дистрибутивов, пофайлово и нет
    path_to_directory = Column(String)
    checksum_alghoritm = Column(String)

# ----------------------------------------------------------------------Dynamic analysis---------------------------------------------------------

class Dynamic_analysis(Base):
    __tablename__ = 'dynamec_analysis'

    id = Column(Integer, primary_key=True, index=True)
    # связать с проектом
    id_project = Column(Integer)
    # статус вставки датчиков - вставлены ли, с ошибками или нет...
    sensors_insertion_status = Column(String)
    # статус с информацие о покрытии, сколько процентов и др.
    coverage_status = Column(String)
    # статус удаления датчиков (когда слишком большой объем файла с сработанными датчиками, удалить повторяющиеся, уточнить у Аси)
    delete_sensors_status = Column(String)


class Dynamic_analysis_history(Base):
    __tablename__ = 'dynamic_analysis_history'

    id = Column(Integer, primary_key=True, index=True)
    # связать с проектом
    id_project = Column(Integer)

    path_to_source = Column(String)
    status = Column(String)
    time = Column(DateTime)
    result = Column(String)
    # описание проведенных действий, какие инструменты, какой порядок действий
    instructions_description = Column(String)
