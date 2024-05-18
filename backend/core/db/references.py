import os

from sqlalchemy import and_
from sqlalchemy.orm import Session

from ..db import models
from ..schemas.references import Reference, ReferenceInDB


def db_get_references(db: Session):
    references = db.query(models.Reference).order_by(models.Reference.order).all()
    if not references:
        return None
    return references


def db_get_reference(reference_id: int, db: Session):
    reference = db.query(models.Reference).filter(models.Reference.id == reference_id).first()
    return reference


def db_create_reference(reference: Reference, db: Session):
    new_reference = models.Reference(
        order=reference.order,
        name=reference.name,
        position=reference.position,
        url=reference.url,
        description=reference.description,
        image=reference.image
    )

    references_to_update = db.query(models.Reference).filter(
        and_(models.Reference.id != new_reference.id, models.Reference.order >= reference.order)
    ).all()
    for ref in references_to_update:
        ref.order += 1
    db.commit()

    db.add(new_reference)
    db.commit()
    db.refresh(new_reference)
    return new_reference


def db_update_reference(reference_id: int,reference: Reference, db: Session):
    existing_reference = db.query(models.Reference).filter(models.Reference.id == reference_id).first()
    old_order = existing_reference.order

    existing_reference.order = reference.order
    existing_reference.name = reference.name
    existing_reference.position = reference.position
    existing_reference.url = reference.url
    existing_reference.description = reference.description
    existing_reference.image = reference.image
    db.commit()
    db.refresh(existing_reference)

    if old_order != reference.order:
        # Decrease order of references with greater old order
        references_to_decrease = db.query(models.Reference).filter(
            and_(models.Reference.order >= old_order, models.Reference.id != existing_reference.id)
        ).all()
        for ref in references_to_decrease:
            ref.order -= 1

        # Increase order of references with greater or equal new order
        references_to_increase = db.query(models.Reference).filter(
            and_(models.Reference.order >= reference.order, models.Reference.id != existing_reference.id)
        ).all()
        for ref in references_to_increase:
            ref.order += 1

        db.commit()

    return existing_reference


def db_delete_reference(reference_id: int, db: Session):
    reference = db.query(models.Reference).filter(models.Reference.id == reference_id).first()
    if not reference:
        return False

    file_path = reference.image
    if os.path.exists(file_path):
        os.remove(file_path)

    deleted_order = reference.order

    db.delete(reference)
    db.commit()

    references_to_decrease = db.query(models.Reference).filter(
        models.Reference.order > deleted_order
    ).all()
    for ref in references_to_decrease:
        ref.order -= 1

    db.commit()
    return True
