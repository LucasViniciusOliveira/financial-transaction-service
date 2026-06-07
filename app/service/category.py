from app.database.models.category import Category
from app.repository.category import CategoryRepository
from app.schemas.category import CreateCategoryRequest


class CategoryService:
    def __init__(self, db):
        self.category_repository = CategoryRepository(db)

    async def create(self, data: CreateCategoryRequest):
        category_dict = {
            "name": data.name,
            "description": data.description,
            "color":data.color,
            "icon":data.icon,
            "user_id": data.user_id,
        }

        category = await self.category_repository.create_entity(
            Category, category_dict
        )
        return {"status": True, "data": category }

    async def find_by_id(self, category_id):
        category = await self.category_repository.get(category_id)
        return {"status": True, "data": category}

    async def get_all(self):
        categories = await self.category_repository.list()
        return {"status": True, "data": categories}

    async def remove(self, category_id):
        category = await self.category_repository.soft_delete(category_id)
        return {"status": True, "data": category}
