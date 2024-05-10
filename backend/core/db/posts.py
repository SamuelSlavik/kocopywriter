from sqlalchemy.orm import Session

from ..schemas.posts import Post as PostSchema
from ..db import models


def db_get_posts(db: Session):
    posts = db.query(models.Post).order_by(models.Post.date).all()
    if not posts:
        return None
    return posts


def db_get_post(post_id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    return post


def db_create_post(post: PostSchema, db: Session):
    new_post = models.Post(
        title=post.title,
        image=post.image,
        short=post.short,
        date=post.date,
        content=post.content
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def db_update_post(post_id: int, post: PostSchema, db: Session):
    existing_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not existing_post:
        return None

    existing_post.title = post.title
    existing_post.image = post.image
    existing_post.short = post.short
    existing_post.date = post.date
    existing_post.content = post.content
    db.commit()
    return existing_post


def db_delete_post(post_id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        return False
    db.delete(post)
    db.commit()
    return True
