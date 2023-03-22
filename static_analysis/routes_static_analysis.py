from fastapi import APIRouter, HTTPException, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import RequestStaticAnalysisStatuses, RequestBinarySearchHisotory, Response
import static_analysis.crud_static_analysis as crud_static_analysis
# import create_statuses, get_statuses, get_statuses_by_project_id, add_to_binary_search_history, remove_statuses_by_project_id

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
    crud_static_analysis.create_statuses(db, request.parameter)
    return Response(code=200, status="Ok", message="Book created successfully").dict(exclude_none=True)


@router_static_analysis.get("/")
async def get(db: Session = Depends(get_db)):
    _statuses = crud_static_analysis.get_statuses(db, 0, 100)
    return Response(code=200, status="ok", message="Success fetch all data", result=_statuses).dict(exclude_none=True)


@router_static_analysis.get("/{project_id}")
async def get_by_project_id(project_id: int, db: Session = Depends(get_db)):
    _statuses = crud_static_analysis.get_statuses_by_project_id(
        db, project_id)
    return Response(code=200, status="ok", message="Success get data by project_id", result=_statuses).dict(exclude_none=True)


@router_static_analysis.delete("/remove_statuses_by_project_id")
async def remove_statuses_by_project_id(project_id: int, db: Session = Depends(get_db)):
    crud_static_analysis.remove_statuses_by_project_id(db, project_id)
    return Response(code=200, status="Ok", message=f"Information about static analysis statuses in project with project_id: {project_id} successfuly deleted")


@router_static_analysis.put("/{id}")
async def update_by_project_id(request: RequestStaticAnalysisStatuses, db: Session = Depends(get_db)):
    _statuses = crud_static_analysis.update_statuses_by_id(
        db, request.parameter)

    return Response(code=200, status="Ok", message=f"Statuses updated successfuly")

# ----------------------------------------------------------------------------------------


@router_static_analysis.get("/get_binary_search_history/")
async def get_binary_search_history(db: Session = Depends(get_db)):
    _binary_search_history = crud_static_analysis.get_binary_search_history(
        db, 0, 100)
    return Response(code=200, status="Ok", message="Success fetch all data", result=_binary_search_history).dict(exclude_none=True)


@router_static_analysis.post("/add_to_binary_search_history")
async def add_to_binary_search_history(request: RequestBinarySearchHisotory, db: Session = Depends(get_db)):
    crud_static_analysis.add_to_binary_search_history(db, request.parameter)
    return Response(code=200, status="Ok", message="Information about binary search added to history successfully").dict(exclude_none=True)
