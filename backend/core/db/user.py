
from sqlalchemy.orm import Session, joinedload
from ..db import models


def db_update_user_email(user_id: int, email: str, db: Session):
    #user = db.query(models.User).filter(models.User.id == user_id).first()
    #if user is None:
     #   return None
    #user.email = email
    #db.commit()
    #db.refresh(user)
    return #user


def db_update_user_password(user_id: int, password: str, db: Session):
    #user = db.query(models.User).filter(models.User.id == user_id).first()
    #if user is None:
     #   return None
    #user.password = password
    #db.commit()
    #db.refresh(user)
    return #user
