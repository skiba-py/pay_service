from fastapi import APIRouter

payments_router = APIRouter(tags=["payments"])


@payments_router.get("/")
async def get_payments():
    return {"message": "Get all payments"}


@payments_router.post("/")
async def create_payment():
    return "OK"
