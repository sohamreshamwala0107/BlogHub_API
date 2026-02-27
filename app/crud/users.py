from sqlalchemy.orm import Session
from app.models.users import Users
from app.schemas.users import UserCreate, UserUpdate
from app.core.security import hash_password


# -----------------------------------
# GET USER BY EMAIL
# -----------------------------------
def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()


# -----------------------------------
# GET USER BY ID
# -----------------------------------
def get_user_by_id(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()


# -----------------------------------
# CREATE USER (REGISTER)
# -----------------------------------
def create_user(db: Session, user: UserCreate):

    # hash plain password
    hashed_pwd = hash_password(user.password)

    db_user = Users(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        hashed_password=hashed_pwd,
        role="user",     # default role
        is_active=True
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# -----------------------------------
# UPDATE USER
# -----------------------------------
def update_user(db: Session, db_user: Users, user_update: UserUpdate):

    if user_update.firstname is not None:
        db_user.firstname = user_update.firstname

    if user_update.lastname is not None:
        db_user.lastname = user_update.lastname

    if user_update.password is not None:
        db_user.hashed_password = hash_password(user_update.password)

    db.commit()
    db.refresh(db_user)

    return db_user


# -----------------------------------
# HARD DELETE USER
# -----------------------------------
def delete_user(db: Session, db_user: Users):
    db.delete(db_user)
    db.commit()
    return True


# -----------------------------------
# SOFT DELETE (Recommended)
# -----------------------------------
def deactivate_user(db: Session, db_user: Users):
    db_user.is_active = False
    db.commit()
    db.refresh(db_user)
    return db_user