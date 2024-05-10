import os
from typing import Optional

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
        name: str = Form(...),
        url: str = Form(...),
        description: str = Form(...),
        image: UploadFile = File(...),
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user)
):
    file_location = os.path.join(config.POST_IMAGES_DIR, image.filename)
    try:
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
        new_reference = Reference(
            name=name,
            url=url,
            description=description,
            image=file_location
        )
        uploaded_image = db_create_reference(new_reference, session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create reference: {str(e)}")

    return uploaded_image


@references_route.put("/update/{reference_id}")
async def update_reference(
        reference_id: int,
        name: str = Form(...),
        url: str = Form(...),
        description: str = Form(...),
        image: Optional[UploadFile] = File(None),
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user)
):
    if image is not None:
        file_location = os.path.join(config.POST_IMAGES_DIR, image.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
    else:
        existing_reference = db_get_reference(reference_id, session)
        file_location = os.path.join(existing_reference.image)

    new_reference = Reference(
        name=name,
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

