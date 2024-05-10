from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .user import get_current_user
from ..db.databases import get_session
from ..db.pricing import db_create_price_list_item, db_get_price_list_items, db_update_price_list_item, \
    db_delete_price_list_item, db_get_price_list_item
from ..schemas.pricing import PriceListItem
from ..schemas.user import User

pricing_route = APIRouter()


@pricing_route.get("")
async def get_price_list_items(session: Session = Depends(get_session)):
    items = db_get_price_list_items(session)
    if not items:
        raise HTTPException(status_code=400, detail="Could not retrieve pricing items")
    return items


@pricing_route.get("/{item_id}")
async def get_price_list_item(item_id: int, session: Session = Depends(get_session)):
    item = db_get_price_list_item(item_id, session)
    if not item:
        raise HTTPException(status_code=400, detail="Could not retrieve pricing item")
    return item

@pricing_route.post("/create")
async def create_price_list_item(item: PriceListItem, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    new_item = db_create_price_list_item(item, session)
    if not new_item:
        raise HTTPException(status_code=400, detail="Could not create pricing item")
    return new_item


@pricing_route.put("/update/{item_id}")
async def update_price_list_item(item_id: int, item: PriceListItem, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    updated_item = db_update_price_list_item(item_id, item, session)

    if not updated_item:
        raise HTTPException(status_code=400, detail="Could not update pricing item")

    return updated_item


@pricing_route.delete("/delete/{item_id}")
async def delete_price_list_item(item_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    if not db_delete_price_list_item(item_id, session):
        raise HTTPException(status_code=400, detail="Could not delete pricing item")
    return {"message": "Item deleted"}
