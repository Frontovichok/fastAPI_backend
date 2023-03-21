from sqlalchemy.orm import Session
from .model_accounts import Account
from schemas import StaticAnalysisStatusesSchema, AddToBinarySearchHisotorySchema
from fastapi.exceptions import HTTPException
from http import HTTPStatus


def get_accounts(db: Session, skip: int = 0, limit: int = 100):
    _accounts = db.query(Account).offset(skip).limit(limit).all()
    if not _accounts:
        raise HTTPException(
            status_code=int(HTTPStatus.NOT_FOUND), detail=f"Static analysis information is not exist"
        )
    return _accounts


def create_account(db: Session, static_analysis_statuses: StaticAnalysisStatusesSchema):
    _accounts = Account(project_id=static_analysis_statuses.project_id)
    db.add(_accounts)
    db.commit()
    db.refresh(_accounts)
    return _accounts


def get_account_by_login(db: Session, login: str):
    _account = db.query(Account).filter(
        Account.login == login).first()
    if not _account:
        raise HTTPException(
            status_code=int(HTTPStatus.NOT_FOUND), detail=f"No static analysis information exist with project_id = {project_id}"
        )
    return _account
