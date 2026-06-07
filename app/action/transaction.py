class TransactionAction:
    def __init__(self, db):
        self.create_transaction = CreateTransaction(db)

    async def create(self, data):
        result = await self.create_transaction.execute(data)
