from http.client import HTTPException

from app.schemas.category import CreateCategoryRequest
from app.service.category import CategoryService


class CategoryAction:
    def __init__(self, db):
        self.category_service = CategoryService(db)

    async def create(self, data: CreateCategoryRequest):
        try:
           result = await self.category_service.create(data)

           if result["status"] == True:
               return result

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro inesperado ao criar a categoria: {str(e)}"
            )

    async def find_by_id(self, category_id: str):
        try:
            result = await self.category_service.find_by_id(category_id)
            if result["status"] == True:
                return result

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro inesperado ao obter a categoria: {str(e)}"
            )

    async def get_all(self):
        try:
            result = await self.category_service.get_all()
            if result["status"] == True:
                return result

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro inesperado ao obter a categoria: {str(e)}"
            )

    async def remove(self, category_id: str):
        try:
            result = await self.category_service.remove(category_id)
            if result["status"] == True:
                return result

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro inesperado ao remover a categoria: {str(e)}"
            )
