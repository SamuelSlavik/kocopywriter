from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

from .user import get_current_user
from ..db.databases import get_session
from ..db.models import User
from ..db.headline import db_create_headline, db_update_headline, db_get_headline
from ..schemas.headline import Headline

headline_route = APIRouter()


@headline_route.get("")
async def get_headline(session: Session = Depends(get_session)):
    headline = db_get_headline(session)
    if not headline:
        raise HTTPException(status_code=400, detail="Could not retrieve headline")
    return headline


@headline_route.post("/create")
async def create_headline(data: Headline, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    headline = db_create_headline(data.text, session)
    return headline


@headline_route.put("/update")
async def update_headline(data: Headline, user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    try:
        new_headline = db_update_headline(data.text, session)
    except:
        raise HTTPException(status_code=400, detail="Could not update the headline")
    return new_headline
