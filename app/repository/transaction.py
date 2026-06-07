from app.service.create_transaction import CreateTransaction


class TransactionRepository:
    def __init__(self, db):
        self.db = db

    create_transaction = CreateTransaction