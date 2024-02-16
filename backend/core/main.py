from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.databases import get_session

from schemas.user import CreateUser
import db.models

app = FastAPI()


@app.post("/api/register")
async def register(user: CreateUser, session: Session = Depends(get_session())):
    # Search database with email, if it returns any user, raise exception
    existing_user = session.query(db.models.User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")




    print("a")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}