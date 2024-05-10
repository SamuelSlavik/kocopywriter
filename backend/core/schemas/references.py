from pydantic import BaseModel


class Reference(BaseModel):
    name: str
    url: str
    description: str
    image: str


class ReferenceInDB(Reference):
    id: int
