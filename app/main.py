import uvicorn
from fastapi import FastAPI
from app.app import get_app
from app.config import settings
from app.logger import logger


def run_api_app() -> None:
    logger.info("Starting API app")
    app = FastAPI(docs_url="/docs", redoc_url="/redoc")
    app.mount(settings.app.app_mount, get_app())
    uvicorn.run(app, host=settings.app.app_host, port=settings.app.app_port, log_config=None)
