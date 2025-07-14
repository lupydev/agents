from fastapi import APIRouter
from .routes.agent import router

api_router = APIRouter()

api_router.include_router(router, tags=["Agent"])
