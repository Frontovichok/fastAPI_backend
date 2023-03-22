from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from datetime import datetime
from sqlalchemy import JSON

T = TypeVar('T')


# общий для всех шаблон с полями ключ-значение, отправляемый в теле POST запроса от клиентов
class BookSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True


class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)

    
class AccountSchema(BaseModel):
    id: int
    firstname: str
    surname: Optional[str] = None
    patronymic: Optional[str] = None
    post: Optional[str] = None
    gender: Optional[str] = None
    cabinet: Optional[str] = None
    phone_number_work: Optional[str] = None
    phone_number_mobile: Optional[str] = None
    email: Optional[str] = None
    status: Optional[str] = None
    access_level: Optional[str] = None
    working_from: Optional[str] = None

    # Нужно для будущей авторизации
    login: Optional[str] = None
    password_hash: Optional[str] = None

    class Config:
        orm_mode = True


class RequestAccount(BaseModel):
    parameter: AccountSchema = Field(...)


class ProjectSchema(BaseModel):
    id: int
    account_id: Optional[int] = None
    # authors = relationship("Account", secondary="")
    name: Optional[str] = None
    company: Optional[str] = None
    sertification_type: Optional[str] = None
    trust_level: Optional[str] = None
    number: Optional[str] = None
    # Привязать к аккаунтам, экспертов может быть несколько
    experts: Optional[str] = None
    solution: Optional[str] = None
    source_directory: Optional[str] = None
    distrib_directory: Optional[str] = None
    documentation_directory: Optional[str] = None
    status: Optional[str] = None
    reports_directory: Optional[str] = None
    # создать связь с работой(полями этой же таблицы), подпроектом которого является данный компонент
    main_component: Optional[str] = None
    # создать связь с компонентами(полями этой же таблицы), которые входят в данную работу
    subcomponents: Optional[str] = None

    class Config:
        orm_mode = True

class RequestProject(BaseModel):
    parameter: ProjectSchema = Field(...)


class StaticAnalysisStatusesSchema(BaseModel):
    # id: Optional[int]=None
    # title: Optional[str]=None
    # description: Optional[str]=None

    id: Optional[int] = None
    # связать с проектом
    project_id: Optional[int] = None
    build_status: Optional[str] = None
    binaries_status: Optional[str] = None
    extra_files_status: Optional[str] = None
    extra_functions_status: Optional[str] = None
    vulnerabilities_status: Optional[str] = None
    programming_languages: List[str]

    class Config:
        orm_mode = True


class RequestStaticAnalysisStatuses(BaseModel):
    parameter: StaticAnalysisStatusesSchema = Field(...)

# Пока не разобрался что конкретно делают GenericModel и Generic[T]
# Судя по документации, GenericModel нужен для повторного использования общей структуры модели, в данном случае для ответов на запросы
# общий для всех шаблон с полями ключ-значение, отправляемыми клиенту


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class BinarySearchHisotorySchema(BaseModel):
    # id: Optional[int]=None
    # title: Optional[str]=None
    # description: Optional[str]=None

    id: Optional[int]
    # связать с проектом
    project_id: Optional[int] = None
    path_to_source_directory: Optional[str] = None
    status: Optional[str] = None
    time: Optional[datetime] = None
    result: Optional[str] = None

    class Config:
        orm_mode = True


class RequestBinarySearchHisotory(BaseModel):
    parameter: BinarySearchHisotorySchema = Field(...)
