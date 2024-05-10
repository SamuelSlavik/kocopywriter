from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Post(BaseModel):
    title: str
    image: Optional[str]
    short: str
    content: str
    date: str


class PostInDB(Post):
    id: int
