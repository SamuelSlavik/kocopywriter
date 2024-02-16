from typing import Union
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Union[str, None] = None
    trusted_user: Union[str, None] = None