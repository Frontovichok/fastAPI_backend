from fastapi import APIRouter, HTTPException, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestProject, Response
import projects.crud_projects as crud_projects

router_projects = APIRouter(
    prefix="/projects",
    tags=["projects"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_projects.post('/create')
async def create(request: RequestProject, db: Session = Depends(get_db)):
    crud_projects.create_project(db, request.parameter)
    return Response(code=200, status="Ok", message="Account created successfully").dict(exclude_none=True)


@router_projects.get("/")
async def get(db: Session = Depends(get_db)):
    _accounts = crud_projects.get_projects(db, 0, 100)
    return Response(code=200, status="ok", message="Success fetch all data", result=_accounts).dict(exclude_none=True)


@router_projects.get("/{project_id}")
async def get_project_by_id(project_id: int, db: Session = Depends(get_db)):
    _account = crud_projects.get_project_by_id(
        db, project_id)
    return Response(code=200, status="ok", message="Success get data by project_id", result=_account).dict(exclude_none=True)


@router_projects.delete("/remove_project_by_id")
async def remove_project_by_id(id: int, db: Session = Depends(get_db)):
    crud_projects.remove_project_by_id(db, id)
    return Response(code=200, status="Ok", message=f"Project with id: {id} successfuly deleted")
