from pydantic import BaseModel


class Brand(BaseModel):
    name: str
    image: str


class BrandInDB(Brand):
    id: int

