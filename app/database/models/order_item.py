from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.database.connection import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    description = Column("description", String, nullable=False)
    quantity = Column("quantity", Integer, nullable=False)
    price = Column("price", Float, nullable=False)
    order_id=Column("order_id", Integer, ForeignKey("orders.id"), nullable=False)

    def __init__(self, order_id, description, quantity, price=0):
        self.order_id = order_id
        self.description = description
        self.quantity = quantity
        self.price = price