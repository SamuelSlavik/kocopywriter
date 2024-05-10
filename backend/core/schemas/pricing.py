from typing import List, Optional

from pydantic import BaseModel


class ItemWithPrice(BaseModel):
    name: str
    price: int


class PriceListItem(BaseModel):
    title: Optional[str]
    description: Optional[str]
    second_description: Optional[str]
    items: Optional[List[ItemWithPrice]]


class PriceListItemInDB(PriceListItem):
    id: int
