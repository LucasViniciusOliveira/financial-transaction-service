from fastapi import APIRouter

transaction_router = APIRouter(prefix="/transaction", tags=["transaction"])

@transaction_router.post("/transaction")
async def transaction():
    return {"message": "Hello World 2"}



