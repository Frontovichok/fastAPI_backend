from fastapi import APIRouter, HTTPException, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestStaticAnalysisStatuses, RequestAddToBinarySearchHistory, Response
from .crud_static_analysis import create_statuses, get_statuses, get_statuses_by_project_id, add_to_binary_search_history

router_static_analysis = APIRouter(
    prefix="/static-analysis",
    tags=["static-analysis"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router_static_analysis.post('/create')
async def create(request: RequestStaticAnalysisStatuses, db: Session = Depends(get_db)):
    create_statuses(db, request.parameter)
    return Response(code=200, status="Ok", message="Book created successfully").dict(exclude_none=True)


@router_static_analysis.get("/")
async def get(db: Session = Depends(get_db)):
    _statuses = get_statuses(db, 0, 100)
    return Response(code=200, status="ok", message="Success fetch all data", result=_statuses).dict(exclude_none=True)


@router_static_analysis.get("/{project_id}")
async def get_by_project_id(project_id: int, db: Session = Depends(get_db)):
    _statuses = get_statuses_by_project_id(
        db, project_id)
    return Response(code=200, status="ok", message="Success get data by project_id", result=_statuses).dict(exclude_none=True)


@router_static_analysis.post("/add_to_binary_search_history")
async def add_to_binary_search_history(request: RequestAddToBinarySearchHistory, db: Session = Depends(get_db)):
    add_to_binary_search_history(db, request.parameter)
    return Response(code=200, status="Ok", message="Information about binary search added to history successfully").dict(exclude_none=True)
