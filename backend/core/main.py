from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
import cloudinary

from .config import config
from .db.databases import get_session, engine
from .db.models import *
from .routes.brands import brands_route
from .routes.images import images_route
from .routes.pricing import pricing_route
from .routes.references import references_route
from .routes.user import user_route
from .routes.headline import headline_route
from .routes.posts import posts_route
from .routes.projects import projects_route

app = FastAPI()

app.include_router(user_route, prefix="/api/user")
app.include_router(images_route, prefix="/api/images")
app.include_router(headline_route, prefix="/api/headline")
app.include_router(pricing_route, prefix="/api/pricing")
app.include_router(brands_route, prefix="/api/brands")
app.include_router(posts_route, prefix="/api/posts")
app.include_router(references_route, prefix="/api/references")
app.include_router(projects_route, prefix="/api/projects")

app.mount("/images", StaticFiles(directory=config.IMAGES_DIR), name="images")

import cloudinary

cloudinary.config(
    cloud_name="dmdksnv3w",
    api_key="493924196852917",
    api_secret="1U8ztZu5jxjDhE-vygMOhlO4v-A"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        config.FRONTEND_URL,
        config.FRONTEND_URL_WWW,
        config.FRONTEND_URL_VERCEL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create tables inside database
Base.metadata.create_all(engine)