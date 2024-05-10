import os
from typing import Optional

from fastapi import HTTPException, Form, UploadFile, File

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..config import config
from ..db.databases import get_session
from ..db.images import db_get_images, db_get_image, db_create_image, db_update_image, db_delete_image
from ..routes.user import get_current_user
from ..schemas.images import Image
from ..schemas.user import User

images_route = APIRouter()

@images_route.get("")
async def get_images(query: str = None, session: Session = Depends(get_session)):
    images = db_get_images(query, session)
    if not images:
        raise HTTPException(status_code=400, detail="Could not retrieve images")
    return images


@images_route.get("/{image_id}")
async def get_image(image_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    print(image_id)
    image = db_get_image(image_id, session)
    if not image:
        raise HTTPException(status_code=400, detail="Could not retrieve image")
    return image


@images_route.post("/create")
async def add_images(
        name: str = Form(...),
        image: UploadFile = File(...),
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user)
):
    file_location = os.path.join(config.POST_IMAGES_DIR, image.filename)
    try:
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
        new_image = Image(url=file_location, name=name)
        uploaded_image = db_create_image(new_image, session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload {image.filename}: {str(e)}")

    return uploaded_image


@images_route.put("/update/{image_id}")
async def update_image(
        image_id: int,
        name: str = Form(...),
        image: Optional[UploadFile] = File(None),
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user)
):
    if image is not None:
        file_location = os.path.join(config.POST_IMAGES_DIR, image.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
    else:
        existing_image = db_get_image(image_id, session)
        file_location = os.path.join(existing_image.url)

    new_image = Image(url=file_location, name=name)
    updated_image = db_update_image(image_id, new_image, session)

    if not updated_image:
        raise HTTPException(status_code=400, detail="Could not update image")

    return updated_image


@images_route.delete("/delete/{image_id}")
async def delete_image(image_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    try:
        result = db_delete_image(image_id, session)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
