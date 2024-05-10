import os

from sqlalchemy.orm import Session

from ..schemas.brands import Brand, BrandInDB
from ..db import models


def db_get_brands(db: Session):
    brands = db.query(models.Brand).order_by(models.Brand.id).all()
    if not brands:
        return None
    return brands


def db_get_brand(brand_id: int, db: Session):
    brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    return brand


def db_create_brand(brand: Brand, db: Session):
    new_brand = models.Brand(name=brand.name, image=brand.image)
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return new_brand


def db_update_brand(brand_id: int, brand: Brand, db: Session):
    existing_brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    existing_brand.name = brand.name
    existing_brand.image = brand.image
    db.commit()
    db.refresh(existing_brand)
    return existing_brand


def db_delete_brand(brand_id: int, db: Session):
    brand = db.query(models.Brand).filter(models.Brand.id == brand_id).first()
    if not brand:
        return False

    file_path = brand.image
    if os.path.exists(file_path):
        os.remove(file_path)

    db.delete(brand)
    db.commit()
    return True
