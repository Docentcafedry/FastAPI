from pydantic import BaseModel, EmailStr
from typing import Annotated
from annotated_types import MinLen, MaxLen
from datetime import datetime


class UserBase(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(15)]
    email: EmailStr


class UserCreate(UserBase):
    password: Annotated[str, MinLen(8), MaxLen(16)]
    join_date: datetime = datetime.utcnow()


class User(UserBase):
    password: bytes
    join_date: datetime = datetime.utcnow()
