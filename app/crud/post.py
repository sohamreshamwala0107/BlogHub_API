from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate


# -----------------------------------
# CREATE POST
# -----------------------------------
def create_post(db: Session, post: PostCreate, user_id: int):
    db_post = Post(
        title=post.title,
        content=post.content,
        user_id=user_id
    )

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post


# -----------------------------------
# GET ALL POSTS
# -----------------------------------
def get_all_posts(db: Session):
    return db.query(Post).all()


# -----------------------------------
# GET POST BY ID
# -----------------------------------
def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


# -----------------------------------
# UPDATE POST
# -----------------------------------
def update_post(db: Session, db_post: Post, post_update: PostUpdate):

    if post_update.title is not None:
        db_post.title = post_update.title

    if post_update.content is not None:
        db_post.content = post_update.content

    db.commit()
    db.refresh(db_post)

    return db_post


# -----------------------------------
# DELETE POST
# -----------------------------------
def delete_post(db: Session, db_post: Post):
    db.delete(db_post)
    db.commit()
    return True