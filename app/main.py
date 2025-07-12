from fastapi import FastAPI
from core.config import settings
from core.db import init_db
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.0.1",
    lifespan=lifespan,
)


@app.get("/")
def read_root():
    return {"message": "Hello agentes"}
