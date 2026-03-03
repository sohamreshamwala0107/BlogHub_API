from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.post import PostCreate, PostUpdate, PostResponse
from app.crud.post import (
    create_post,
    get_all_posts,
    get_post_by_id,
    update_post,
    delete_post
)
from app.core.security import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)
# CREATE POST (Login Required)
@router.post("/", response_model=PostResponse)
def create_post_route(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_post(db, post, current_user.id)

# GET ALL POSTS (Public)
@router.get("/", response_model=list[PostResponse])
def get_all_posts_route(db: Session = Depends(get_db)):
    return get_all_posts(db)


# GET SINGLE POST (Public)
@router.get("/{post_id}", response_model=PostResponse)
def get_post_route(post_id: int, db: Session = Depends(get_db)):

    db_post = get_post_by_id(db, post_id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    return db_post


# UPDATE POST (Author Only)
@router.put("/{post_id}", response_model=PostResponse)
def update_post_route(
    post_id: int,
    post_update: PostUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    db_post = get_post_by_id(db, post_id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    if db_post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")

    return update_post(db, db_post, post_update)


# DELETE POST (Author OR Admin)
@router.delete("/{post_id}")
def delete_post_route(
    post_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    db_post = get_post_by_id(db, post_id)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    if db_post.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    delete_post(db, db_post)

    return {"message": "Post deleted successfully"}