from pydantic import BaseModel
from datetime import datetime


# ---------------- BASE ----------------
class PostBase(BaseModel):
    title: str
    content: str


# ---------------- CREATE ----------------
class PostCreate(PostBase):
    pass


# ---------------- UPDATE ----------------
class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


# ---------------- RESPONSE ----------------
class PostResponse(PostBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime | None = None

    # class Config:
    #     orm_mode = True

    model_config = {
        "from_attributes": True
        }