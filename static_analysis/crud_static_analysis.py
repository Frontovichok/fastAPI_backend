from sqlalchemy.orm import Session
from static_analysis.model_static_analysis import Static_analysis, Binary_search_history
from schemas import StaticAnalysisStatusesSchema, BinarySearchHisotorySchema
from fastapi.exceptions import HTTPException
from http import HTTPStatus


def get_statuses(db: Session, skip: int = 0, limit: int = 100):
    _statuses = db.query(Static_analysis).offset(skip).limit(limit).all()
    if not _statuses:
        raise HTTPException(
            status_code=int(HTTPStatus.NOT_FOUND), detail=f"Static analysis information is not exist"
        )
    return _statuses


def create_statuses(db: Session, static_analysis_statuses: StaticAnalysisStatusesSchema):
    _statuses = Static_analysis(project_id=static_analysis_statuses.project_id,
                                build_status=static_analysis_statuses.build_status,
                                binaries_status=static_analysis_statuses.binaries_status, extra_files_status=static_analysis_statuses.extra_files_status,
                                extra_functions_status=static_analysis_statuses.extra_functions_status,
                                vulnerabilities_status=static_analysis_statuses.vulnerabilities_status,
                                programming_languages=static_analysis_statuses.programming_languages)
    db.add(_statuses)
    db.commit()
    db.refresh(_statuses)
    return _statuses


def get_statuses_by_project_id(db: Session, project_id: int):
    _statuses = db.query(Static_analysis).filter(
        Static_analysis.project_id == project_id).first()
    if not _statuses:
        raise HTTPException(
            status_code=int(HTTPStatus.NOT_FOUND), detail=f"No static analysis information exist with project_id = {project_id}"
        )
    return _statuses


def remove_statuses_by_project_id(db: Session, project_id: int):
    _statuses = get_statuses_by_project_id(db=db, project_id=project_id)
    if not _statuses:
        raise HTTPException(
            status_code=int(HTTPStatus.NOT_FOUND), detail=f"No data with this project_id"
        )
    print(_statuses)
    db.delete(_statuses)
    db.commit()


# ------------------------------------------------------------


def get_binary_search_history(db: Session, skip: int = 0, limit: int = 100):
    print("get_binary_search_history 1")
    _binary_search_history = db.query(
        Binary_search_history).offset(skip).limit(limit).all()
    print("get_binary_search_history 2 ", _binary_search_history)
    if not _binary_search_history:
        print("get_binary_search_history 3")
        raise HTTPException(
            status_code=int(HTTPStatus.NOT_FOUND), detail=f"Binary search history is not exist"
        )
    return _binary_search_history


def add_to_binary_search_history(db: Session, add_to_binary_search: BinarySearchHisotorySchema):
    _data = Binary_search_history(project_id=add_to_binary_search.project_id,
                                  path_to_source_directory=add_to_binary_search.path_to_source_directory,
                                  status=add_to_binary_search.status,
                                  time=add_to_binary_search.time,
                                  result=add_to_binary_search.result)
    db.add(_data)
    db.commit()
    db.refresh(_data)
    return _data
