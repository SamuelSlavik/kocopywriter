import os

from sqlalchemy.orm import Session
from sqlalchemy import and_

from ..db import models

from ..schemas.projects import Project, ProjectInDB


def db_get_projects(db: Session):
    projects = db.query(models.Project).order_by(models.Project.order).all()
    if not projects:
        return None
    return projects


def db_get_project(project_id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        return None
    return project


def db_create_project(project: Project, db: Session):
    new_project = models.Project(
        order=project.order,
        name=project.name,
        url=project.url,
        task=project.task,
        description=project.description,
        images=project.images,
    )

    projects_to_update = db.query(models.Project).filter(
        and_(models.Project.id != new_project.id, models.Project.order >= project.order)
    ).all()
    for project in projects_to_update:
        project.order += 1
    db.commit()

    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def db_update_project(project_id: int, project: Project, db: Session):
    existing_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    old_order = existing_project.order

    existing_project.order = project.order
    existing_project.name = project.name
    existing_project.url = project.url
    existing_project.task = project.task
    existing_project.description = project.description
    existing_project.images = project.images
    db.commit()
    db.refresh(existing_project)

    if old_order != project.order:
        projects_to_decrease = db.query(models.Project).filter(
            and_(models.Project.order >= old_order, models.Project.id != existing_project.id)
        ).all()
        for project in projects_to_decrease:
            project.order -= 1

        projects_to_increase = db.query(models.Project).filter(
            and_(models.Project.order >= project.order, models.Project.id != existing_project.id)
        ).all()
        for project in projects_to_increase:
            project.order += 1

        db.commit()

    return existing_project


def db_delete_project(project_id: int, db: Session):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        return False

    file_path = project.image
    if os.path.exists(file_path):
        os.remove(file_path)

    deleted_order = project.order

    db.delete(project)
    db.commit()

    projects_to_decrease = db.query(models.Project).filter(
        models.Project.order > deleted_order
    ).all()
    for project in projects_to_decrease:
        project.order -= 1

    db.commit()
    return True
