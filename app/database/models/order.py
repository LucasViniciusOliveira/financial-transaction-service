from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.connection import Base

class Order(Base):
    __tablename__ = "orders"

    # STATUS_ORDER = (
    #     ("PENDING", "PENDING"),
    #     ("CANCELED", "CANCELED"),
    #     ("COMPLETED", "COMPLETED"),
    # )

    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    status = Column("status", String, nullable=False)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    amount = Column("amount", String, nullable=False)

    def __init__(self, user_id, status="PENDING", amount=0):
        self.user_id = user_id
        self.status = status
        self.amount = amount