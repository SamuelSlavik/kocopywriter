import os
from sqlalchemy.orm import Session

from ..schemas.images import Image as SchemaImage  # Renamed SchemaImage for clarity
from ..db import models


def db_get_images(query: str, db: Session):
    query = query.strip() if query else None
    if query:
        images = db.query(models.Image).filter(models.Image.name.ilike(f"%{query}%")).order_by(models.Image.name).all()
    else:
        images = db.query(models.Image).order_by(models.Image.name).all()
    if not images:
        return None
    return images


def db_get_image(image_id: int, db: Session):
    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    return image


def db_create_image(image: SchemaImage, db: Session):
    new_image = models.Image(url=image.url, name=image.name)
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    return new_image


def db_update_image(image_id: int, image: SchemaImage, db: Session):
    existing_image = db.query(models.Image).filter(models.Image.id == image_id).first()
    existing_image.url = image.url
    existing_image.name = image.name
    db.commit()
    db.refresh(existing_image)
    return existing_image


def db_delete_image(image_id: int, db: Session):
    image = db.query(models.Image).filter(models.Image.id == image_id).first()
    if not image:
        return False

    file_path = image.url
    if os.path.exists(file_path):
        os.remove(file_path)

    db.delete(image)
    db.commit()
    return True
