from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db.databases import get_session
from ..db.posts import db_get_posts, db_get_post, db_create_post, db_update_post, db_delete_post
from ..routes.user import get_current_user
from ..schemas.posts import Post
from ..schemas.user import User

posts_route = APIRouter()


@posts_route.get("/")
async def get_posts(session: Session = Depends(get_session)):
    posts = db_get_posts(session)
    if not posts:
        raise HTTPException(status_code=400, detail="Could not retrieve posts")
    return posts


@posts_route.get("/{post_id}")
async def get_post(post_id: int, session: Session = Depends(get_session)):
    post = db_get_post(post_id, session)
    if not post:
        raise HTTPException(status_code=400, detail="Could not retrieve post")
    return post


@posts_route.post("/create")
async def create_post(post: Post, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    new_post = db_create_post(post, session)
    if not new_post:
        raise HTTPException(status_code=400, detail="Could not create post")
    return new_post


@posts_route.put("/update/{post_id}")
async def update_post(post_id: int, post: Post, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    updated_post = db_update_post(post_id, post, session)
    if not updated_post:
        raise HTTPException(status_code=400, detail="Could not update post")
    return updated_post


@posts_route.delete("/delete/{post_id}")
async def delete_post(post_id: int):
    try:
        result = db_delete_post(post_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail="Could not delete post")


