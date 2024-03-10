from fastapi_users import schemas
from typing import Optional
from datetime import datetime


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    first_name: Optional[str]
    birthdate: Optional[str]
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    registered_at: Optional[datetime]

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    first_name: Optional[str]
    birthdate: Optional[str]
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    username: str
    first_name: Optional[str]
    birthdate: Optional[str]
    registered_at: Optional[datetime]
