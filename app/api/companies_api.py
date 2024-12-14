from fastapi import APIRouter

companies_router = APIRouter(tags=["companies"])


@companies_router.get("/")
async def get_all_companies():
    return {"message": "Get all companies"}


@companies_router.post("/")
async def create_new_company():
    return "OK"
