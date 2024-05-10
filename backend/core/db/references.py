import os

from sqlalchemy.orm import Session

from ..db import models
from ..schemas.references import Reference, ReferenceInDB


def db_get_references(db: Session):
    references = db.query(models.Reference).order_by(models.Reference.id).all()
    if not references:
        return None
    return references


def db_get_reference(reference_id: int, db: Session):
    reference = db.query(models.Reference).filter(models.Reference.id == reference_id).first()
    return reference


def db_create_reference(reference: Reference, db: Session):
    new_reference = models.Reference(
        name=reference.name,
        url=reference.url,
        description=reference.description,
        image=reference.image
    )
    db.add(new_reference)
    db.commit()
    db.refresh(new_reference)
    return new_reference


def db_update_reference(reference_id: int,reference: Reference, db: Session):
    existing_reference = db.query(models.Reference).filter(models.Reference.id == reference_id).first()
    existing_reference.name = reference.name
    existing_reference.url = reference.url
    existing_reference.description = reference.description
    existing_reference.image = reference.image
    db.commit()
    db.refresh(existing_reference)
    return existing_reference


def db_delete_reference(reference_id: int, db: Session):
    reference = db.query(models.Reference).filter(models.Reference.id == reference_id).first()
    if not reference:
        return False

    file_path = reference.image
    if os.path.exists(file_path):
        os.remove(file_path)

    db.delete(reference)
    db.commit()
    return True
