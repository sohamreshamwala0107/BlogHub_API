from pydantic import BaseModel, EmailStr
from datetime import datetime


# ---------------- REGISTER ----------------
class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str   # plain password


# ---------------- RESPONSE ----------------
class UserResponse(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    class Config:   # Capital C
        orm_mode = True


# ---------------- UPDATE ----------------
class UserUpdate(BaseModel):
    firstname: str | None = None
    lastname: str | None = None
    password: str | None = None   # plain password


# ---------------- LOGIN ----------------
class UserLogin(BaseModel):
    email: EmailStr
    password: str   # plain password


# ---------------- TOKEN ----------------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int | None = None
    role: str | None = None