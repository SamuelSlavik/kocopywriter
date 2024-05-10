import os
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, File, Form, UploadFile
from sqlalchemy.orm import Session

from .user import get_current_user
from ..config import config
from ..db.brands import db_get_brands, db_get_brand, db_delete_brand, db_create_brand, db_update_brand
from ..db.databases import get_session
from ..schemas.brands import Brand
from ..schemas.user import User

brands_route = APIRouter()


@brands_route.get("/")
async def get_all_brands(session: Session = Depends(get_session)):
    brands = db_get_brands(session)
    if not brands:
        raise HTTPException(status_code=400, detail="Could not retrieve brands")
    return brands


@brands_route.get("/{brand_id}")
async def get_brand(brand_id: int, session: Session = Depends(get_session)):
    brand = db_get_brand(brand_id, session)
    if not brand:
        raise HTTPException(status_code=400, detail="Could not retrieve brand")
    return brand


@brands_route.post("/create")
async def create_brand(
        name: str = Form(...),
        image: UploadFile = File(...),
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user)
):
    file_location = os.path.join(config.BRANDS_IMAGES_DIR, image.filename)
    try:
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
        new_brand = Brand(name=name, image=file_location)
        uploaded_brand = db_create_brand(new_brand, session)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return uploaded_brand


@brands_route.put("/update/{brand_id}")
async def update_brand(
        brand_id: int,
        name: str = Form(...),
        image: Optional[UploadFile] = File(None),
        session: Session = Depends(get_session),
        user: User = Depends(get_current_user)
):
    if image is not None:
        file_location = os.path.join(config.BRANDS_IMAGES_DIR, image.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(image.file.read())
    else:
        existing_brand = db_get_brand(user.id, session)
        file_location = os.path.join(existing_brand.image)

    new_brand = Brand(name=name, image=file_location)
    updated_brand = db_update_brand(brand_id, new_brand, session)
    return updated_brand


@brands_route.delete("/delete/{brand_id}")
async def delete_brand(brand_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    try:
        result = db_delete_brand(brand_id, session)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not delete brand")
