from fastapi import APIRouter, Request
from app.schemas.misc_schemas import HealthcheckSchema
from app.config import settings

router = APIRouter()


@router.get("/healthcheck", response_model=HealthcheckSchema)
async def healthcheck(request: Request):
    return HealthcheckSchema(status="OK", version=settings.app.app_version)
