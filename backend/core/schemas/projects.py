from typing import Optional

from pydantic import BaseModel


class Project(BaseModel):
    order: int
    name: str
    url: Optional[str]
    task: str
    description: str
    image: str


class ProjectInDB(Project):
    id: int