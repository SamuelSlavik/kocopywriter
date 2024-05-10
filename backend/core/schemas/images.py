import string

from pydantic import BaseModel


class Image(BaseModel):
    url: str
    name: str


class ImageInDB(Image):
    id: int
