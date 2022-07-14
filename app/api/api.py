from api.endpoints import render
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(render.router, tags=["render"])
