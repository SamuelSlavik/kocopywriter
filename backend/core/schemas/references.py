from pydantic import BaseModel


class Reference(BaseModel):
    order: int
    name: str
    position: str
    url: str
    description: str
    image: str


class ReferenceInDB(Reference):
    id: int
