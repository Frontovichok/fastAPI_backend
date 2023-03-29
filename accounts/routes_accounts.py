from fastapi import APIRouter, HTTPException, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestAccount, Response
import accounts.crud_accounts as crud_accounts

router_accounts = APIRouter(
    prefix="/accounts",
    tags=["accounts"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_accounts.post('/create')
async def create(request: RequestAccount, db: Session = Depends(get_db)):
    crud_accounts.create_account(db, request.parameter)
    return Response(code=200, status="Ok", message="Account created successfully").dict(exclude_none=True)


@router_accounts.get("/")
async def get(db: Session = Depends(get_db)):
    _accounts = crud_accounts.get_accounts(db, 0, 100)
    return Response(code=200, status="ok", message="Success fetch all data", result=_accounts).dict(exclude_none=True)


@router_accounts.get("/{account_login}")
async def get_account_by_login(account_login: str, db: Session = Depends(get_db)):
    _account = crud_accounts.get_account_by_login(
        db, account_login)
    return Response(code=200, status="ok", message="Success get data by project_id", result=_account).dict(exclude_none=True)


@router_accounts.delete("/remove_account_by_login")
async def remove_account_by_login(login: str, db: Session = Depends(get_db)):
    crud_accounts.remove_account_by_login(db, login)
    return Response(code=200, status="Ok", message=f"Account with login: {login} successfuly deleted")
