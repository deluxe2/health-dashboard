from contextlib import asynccontextmanager
from beanie import init_beanie
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from health_dashboard import models
from health_dashboard.settings import settings


async def startup(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(settings.db_url)
    await init_beanie(
        database=app.mongodb_client[settings.db_name], document_models=models.models
    )


async def shutdown(app: FastAPI):
    app.mongodb_client.close()


@asynccontextmanager
async def db(app: FastAPI):
    await startup(app)
    yield
    await shutdown(app)
