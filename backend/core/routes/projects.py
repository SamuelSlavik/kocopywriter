import os
from typing import Optional, List

from cloudinary.uploader import cloudinary
from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile, File
from sqlalchemy.orm import Session

from .user import get_current_user
from ..db.databases import get_session
from ..schemas.user import User
from ..schemas.projects import Project, ProjectInDB
from ..db.projects import *

projects_route = APIRouter()


@projects_route.get("/")
async def get_projects(session: Session = Depends(get_session)):
    projects = db_get_projects(session)
    if not projects:
        raise HTTPException(status_code=400, detail="Could not retrieve projects")
    return projects


@projects_route.get("/{project_id}")
async def get_project(project_id: int, session: Session = Depends(get_session)):
    project = db_get_project(project_id, session)
    if not project:
        raise HTTPException(status_code=400, detail="Could not retrieve project")
    return project


@projects_route.post("/create")
async def create_project(
        order: int = Form(...),
        name: str = Form(...),
        url: Optional[str] = Form(None),
        task: str = Form(...),
        description: str = Form(...),
        images: List[UploadFile] = Form(...),
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user),
):
    try:
        image_urls = []
        for image in images:
            upload_result = cloudinary.uploader.upload(image.file)
            image_urls.append(upload_result["secure_url"])

        new_project = Project(
            order=order,
            name=name,
            url=url,
            task=task,
            description=description,
            image=image_urls,
        )
        uploaded_project = db_create_project(new_project, session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not create project: {str(e)}")

    return uploaded_project


@projects_route.put("/update/{project_id}")
async def update_project(
        project_id: int,
        order: int = Form(...),
        name: str = Form(...),
        url: Optional[str] = Form(None),
        task: str = Form(...),
        description: str = Form(...),
        images: Optional[List[UploadFile]] = File(None),
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user),
):
    if images is not None:
        image_urls = []
        try:
            for image in images:
                upload_result = cloudinary.uploader.upload(image.file)
                image_urls.append(upload_result["secure_url"])
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Could not retrieve image: {str(e)}")
    else:
        existing_project = db_get_project(project_id, session)
        image_urls = existing_project.image if existing_project else []

    new_project = Project(
        order=order,
        name=name,
        url=url,
        task=task,
        description=description,
        image=image_urls,
    )
    updated_project = db_update_project(project_id, new_project, session)
    if not updated_project:
        raise HTTPException(status_code=400, detail="Could not update project")
    return updated_project


@projects_route.delete("/delete/{project_id}")
async def delete_project(project_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    try:
        result = db_delete_project(project_id, session)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Could not delete project: {str(e)}")
