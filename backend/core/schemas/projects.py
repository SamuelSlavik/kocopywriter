from typing import Optional, List

from pydantic import BaseModel


class Project(BaseModel):
    order: int
    name: str
    url: Optional[str]
    task: str
    description: str
    image: List[str]


class ProjectInDB(Project):
    id: int