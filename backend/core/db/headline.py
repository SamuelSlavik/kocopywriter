from sqlalchemy.orm import Session
from .models import Headline
from fastapi import HTTPException


def db_get_headline(db: Session):
    return db.query(Headline).filter(Headline.id == 1).first()


def db_create_headline(text: str, db: Session):
    headline = Headline(text=text)
    db.add(headline)
    db.commit()
    db.refresh(headline)
    return headline


def db_update_headline(text: str, db: Session):
    existing_headline = db.query(Headline).filter(Headline.id == 1).first()
    existing_headline.text = text
    db.commit()
    db.refresh(existing_headline)
    return existing_headline
