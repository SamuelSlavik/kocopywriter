from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class User(BaseModel):
    id: UUID
    email: str
    password: str
    trusted: bool

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
    reset_password_token: Optional[str] = None
    created_at: datetime
    last_change: datetime

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    email: str
    password: str
