from sqlalchemy.orm import Session
from .model_projects import Projects
from schemas import ProjectSchema
from fastapi.exceptions import HTTPException
from http import HTTPStatus


def get_projects(db: Session, skip: int = 0, limit: int = 100):
    _projects = db.query(Projects).offset(skip).limit(limit).all()
    if not _projects:
        raise HTTPException(
            status_code=int(HTTPStatus.NOT_FOUND), detail=f"Static analysis information is not exist"
        )
    return _projects


def create_project(db: Session, project: ProjectSchema):
    _project = Projects(id=project.id,
                        account_id=project.account_id,
                        name=project.name,
                        company=project.company,
                        sertification_type=project.sertification_type,
                        trust_level=project.trust_level,
                        number=project.number,
                        experts=project.experts,
                        solution=project.solution,
                        source_directory=project.source_directory,
                        distrib_directory=project.distrib_directory,
                        documentation_directory=project. documentation_directory,
                        status=project. status,
                        reports_directory=project.reports_directory,
                        main_component=project. main_component,
                        subcomponents=project. subcomponents)
    db.add(_project)
    db.commit()
    db.refresh(_project)
    return _project


def get_project_by_id(db: Session, id: int):
    _project = db.query(Projects).filter(
        Projects.id == id).first()
    if not _project:
        raise HTTPException(
            status_code=int(HTTPStatus.NOT_FOUND), detail=f"No static analysis information exist with id = {id}"
        )
    return _project
