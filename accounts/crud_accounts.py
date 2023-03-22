from sqlalchemy.orm import Session
from .model_accounts import Account
from schemas import AccountSchema
from fastapi.exceptions import HTTPException
from http import HTTPStatus


def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    _accounts = db.query(Account).offset(skip).limit(limit).all()
    if not _accounts:
        raise HTTPException(
            status_code=int(HTTPStatus.NOT_FOUND), detail=f"Accounts do not exist"
        )
    return _accounts


def create_account(db: Session, account: AccountSchema):
    _account = Account(id=account.id,
                       firstname=account.firstname,
                       surname=account.surname,
                       patronymic=account.patronymic,
                       post=account.post,
                       gender=account.gender,
                       cabinet=account.cabinet,
                       phone_number_work=account.phone_number_work,
                       phone_number_mobile=account.phone_number_mobile,
                       email=account.email,
                       status=account.status,
                       access_level=account.access_level,
                       working_from=account.working_from,
                       login=account.login,
                       password_hash=account.password_hash)
    db.add(_account)
    db.commit()
    db.refresh(_account)
    return _account


def get_account_by_login(db: Session, login: str):
    _account = db.query(Account).filter(
        Account.login == login).first()
    if not _account:
        raise HTTPException(
            status_code=int(HTTPStatus.NOT_FOUND), detail=f"No static analysis information exist with project_id = {_account}"
        )
    return _account
