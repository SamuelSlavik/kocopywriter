from typing import Optional, List

from pydantic import BaseModel


class Project(BaseModel):
    order: int
    name: str
    task: str
    description: str
    images: List[str]


class ProjectInDB(Project):
    id: int