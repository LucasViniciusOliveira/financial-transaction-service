from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.action.transaction import TransactionAction
from app.database.connection import get_db


transaction_router = APIRouter(prefix="/transaction", tags=["transaction"])

@transaction_router.post("/transaction")
async def transaction(
    data,
    db: AsyncSession = Depends(get_db)
):
    action = TransactionAction(db)
    return await action.create(data)



