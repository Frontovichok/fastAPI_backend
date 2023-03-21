# Create. Read. Update. Delete
# функции работы с базой данных

from sqlalchemy.orm import Session
from model import Book
from schemas import BookSchema

# Get all book data


def get_book(db: Session, skip: int = 0, limit: int = 100):
    # offset(skip) - пропустить skip строк
    # limit(limit) - вернуть limit значений
    # .all() - вернуть все найденные записи ( а не только первую например, как в случае с first())
    return db.query(Book).offset(skip).limit(limit).all()


# def get_statuses(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Static_analysis).offset(skip).limit(limit).all()


# def create_statuses(db: Session, static_analysis_statuses: StaticAnalysisStatusesSchema):
#     _statuses = Static_analysis(build_status=static_analysis_statuses.build_status,
#                             binaries_status=static_analysis_statuses.binaries_status, extra_files_status=static_analysis_statuses.extra_files_status,
#                             extra_functions_status=static_analysis_statuses.extra_functions_status,
#                             vulnerabilities_status=static_analysis_statuses.vulnerabilities_status,
#                             programming_languages=static_analysis_statuses.programming_languages)
#     # print("book: ", book)
#     # print("_book: ", _book)

#     # как в Git
#     # add - добавляет изменения в сессию, но не отправляет запрос в БД
#     db.add(_statuses)
#     # сессия откроет транзакцию, отправит запросы и выполнит commit
#     db.commit()

#     db.refresh(_statuses)
#     return _statuses

# Get by id book data


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

# Create book data


def create_book(db: Session, book: BookSchema):
    _book = Book(title=book.title, description=book.description)
    # print("book: ", book)
    # print("_book: ", _book)

    # как в Git
    # add - добавляет изменения в сессию, но не отправляет запрос в БД
    db.add(_book)
    # сессия откроет транзакцию, отправит запросы и выполнит commit
    db.commit()

    db.refresh(_book)
    return _book

# Remove book data


def remove_book(db: Session, book_id: int):
    _book = get_book_by_id(db=db, book_id=book_id)
    db.delete(_book)
    db.commit()

# Update book data


def update_book(db: Session, book_id: int, title: str, description: str):
    _book = get_book_by_id(db=db, book_id=book_id)
    _book.title = title
    _book.description = description
    db.commit()
    db.refresh(_book)
    return _book