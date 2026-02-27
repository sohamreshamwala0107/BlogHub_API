from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.users import UserResponse, UserUpdate
from app.crud.users import (
    get_user_by_id,
    update_user,
    delete_user,
    deactivate_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# -----------------------------------
# GET USER BY ID
# -----------------------------------
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):

    db_user = get_user_by_id(db, user_id)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return db_user


# -----------------------------------
# UPDATE USER
# -----------------------------------
@router.put("/{user_id}", response_model=UserResponse)
def update_user_route(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db)
):

    db_user = get_user_by_id(db, user_id)

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    updated_user = update_user(db, db_user, user_update)
    return updated_user


# -----------------------------------
# SOFT DELETE USER
# -----------------------------------
@router.delete("/{user_id}")
def deactivate_user_route(user_id: int, db: Session = Depends(get_db)):

    db_user = get_user_by_id(db, user_id)

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    deactivate_user(db, db_user)

    return {"message": "User deactivated successfully"}


# -----------------------------------
# HARD DELETE USER
# -----------------------------------
@router.delete("/hard/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):

    db_user = get_user_by_id(db, user_id)

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    delete_user(db, db_user)

    return {"message": "User deleted permanently"}

# -----------------------------------
# GET ALL USERS
# -----------------------------------
@router.get("/", response_model=list[UserResponse])
def get_all_users_route(db: Session = Depends(get_db)):
    from app.crud.users import get_all_users  # make sure this exists
    users = get_all_users(db)
    return users