from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.transaction import TransactionRepository


class CreateTransaction:
    def __init__(self, db: AsyncSession):
        self.transaction_repository = TransactionRepository(db)

    async def create(self, data):
        # Preparar os dados

        # Verificar parcelamento

        # Incluir os dados
        return {"success": True}



