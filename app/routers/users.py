from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.users import UserResponse, UserUpdate
from app.crud.users import (
    get_user_by_id,
    update_user,
    delete_user,
    deactivate_user,
    get_all_users
)
from app.core.security import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# GET USER BY ID (Self or Admin)
@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    if current_user.id != user_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    db_user = get_user_by_id(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user

# UPDATE USER (Self Only)
@router.put("/{user_id}", response_model=UserResponse)
def update_user_route(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not authorized")

    db_user = get_user_by_id(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return update_user(db, db_user, user_update)


# SOFT DELETE (Self or Admin)
@router.delete("/{user_id}")
def deactivate_user_route(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    if current_user.id != user_id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    db_user = get_user_by_id(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    deactivate_user(db, db_user)

    return {"message": "User deactivated successfully"}

# HARD DELETE (Admin Only)
@router.delete("/hard/{user_id}")
def delete_user_route(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    db_user = get_user_by_id(db, user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    delete_user(db, db_user)

    return {"message": "User deleted permanently"}

# GET ALL USERS (Admin Only)
@router.get("/", response_model=list[UserResponse])
def get_all_users_route(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")

    return get_all_users(db)