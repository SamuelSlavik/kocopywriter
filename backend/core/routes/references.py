import os
from typing import Optional

from cloudinary.uploader import cloudinary
from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile, File
from sqlalchemy.orm import Session

from .user import get_current_user
from ..config import config
from ..db.databases import get_session
from ..db.references import db_get_references, db_get_reference, db_create_reference, db_update_reference, \
    db_delete_reference
from ..schemas.references import Reference
from ..schemas.user import User

references_route = APIRouter()


@references_route.get("/")
async def get_references(session: Session = Depends(get_session)):
    references = db_get_references(session)
    if not references:
        raise HTTPException(status_code=400, detail="Could not retrieve references")
    return references


@references_route.get("/{reference_id}")
async def get_reference(reference_id: int, session: Session = Depends(get_session)):
    reference = db_get_reference(reference_id, session)
    if not reference:
        raise HTTPException(status_code=400, detail="Could not retrieve reference")
    return reference


@references_route.post("/create")
async def create_reference(
        order: int = Form(...),
        name: str = Form(...),
        position: str = Form(...),
        url: str = Form(...),
        description: str = Form(...),
        image: UploadFile = Form(...),
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user)
):
    try:
        file_location = cloudinary.uploader.upload(image.file)
        new_reference = Reference(
            order=order,
            name=name,
            position=position,
            url=url,
            description=description,
            image=file_location["secure_url"],
        )
        uploaded_image = db_create_reference(new_reference, session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create reference: {str(e)}")

    return uploaded_image


@references_route.put("/update/{reference_id}")
async def update_reference(
        reference_id: int,
        order: int = Form(...),
        name: str = Form(...),
        position: str = Form(...),
        url: str = Form(...),
        description: str = Form(...),
        image: Optional[UploadFile] = Form(None),
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user)
):
    if image is not None:
        try:
            file_location = cloudinary.uploader.upload(image.file)
            file_location = file_location["secure_url"]
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Could not retrieve image: {str(e)}")
    else:
        existing_reference = db_get_reference(reference_id, session)
        file_location = os.path.join(existing_reference.image)

    new_reference = Reference(
        order=order,
        name=name,
        position=position,
        url=url,
        description=description,
        image=file_location
    )
    updated_reference = db_update_reference(reference_id, new_reference, session)
    if not updated_reference:
        raise HTTPException(status_code=400, detail="Could not update reference")
    return updated_reference


@references_route.delete("/delete/{reference_id}")
async def delete_reference(reference_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    try:
        result = db_delete_reference(reference_id, session)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

