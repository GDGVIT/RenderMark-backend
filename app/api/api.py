from api.endpoints import render, upload
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(render.router, tags=["render"])
api_router.include_router(upload.router, tags=["image-to-link"])
