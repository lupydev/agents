from fastapi import FastAPI
from core.config import settings
from core.db import init_db
from contextlib import asynccontextmanager
from api.main import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.0.1",
    lifespan=lifespan,
)

app.include_router(api_router, prefix=settings.API)
