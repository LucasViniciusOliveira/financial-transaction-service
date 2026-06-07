from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.action.category import CategoryAction
from app.database.connection import get_db
from app.schemas.category import CreateCategoryRequest

category_router = APIRouter(prefix="/categories", tags=["categories"])

@category_router.post("")
async def create_category(
    data: CreateCategoryRequest,
    db: AsyncSession = Depends(get_db)

):
    action = CategoryAction(db)
    return await action.create(data)

@category_router.get("/{category_id}")
async def find_by_id(
    category_id: str,
    db: AsyncSession = Depends(get_db)
):
    action = CategoryAction(db)
    return await action.find_by_id(category_id)

@category_router.get("")
async def get_all(
    db: AsyncSession = Depends(get_db)
):
    action = CategoryAction(db)
    return await action.get_all()

@category_router.delete("/{category_id}")
async def remove(
    category_id: str,
    db: AsyncSession = Depends(get_db)
):
    action = CategoryAction(db)
    return await action.remove(category_id)