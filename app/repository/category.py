from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import BaseRepository
from app.database.models.category import Category


class CategoryRepository(BaseRepository[Category]):
    def __init__(self, db: AsyncSession):
        super().__init__(db, Category)




