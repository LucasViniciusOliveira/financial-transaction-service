from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID

from app.database.base import Base

class TransactionCategories(Base):
    __tablename__ = "transaction_categories"

    Column(
        "transaction_id",
        UUID(as_uuid=True),
        ForeignKey("transactions.id"),
        primary_key=True,
    ),

    Column(
        "category_id",
        UUID(as_uuid=True),
        ForeignKey("categories.id"),
        primary_key=True,
    )
