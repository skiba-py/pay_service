from fastapi import APIRouter

payments_router = APIRouter(tags=["payments"])


@payments_router.get("")
async def get_payments():
    return {"message": "Get all payments"}


@payments_router.get("/{payment_id}")
async def get_payment_by_id():
    return {"message": "Get payment by id"}


@payments_router.post("/base")
async def create_payments():
    return "OK"


# @payments_router.post("/sbp")
# async def create_sbp_payment():
#     return "OK"
