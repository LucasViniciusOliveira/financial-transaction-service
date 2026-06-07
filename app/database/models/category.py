import uuid

from sqlalchemy import (
    Boolean,
    Column,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database.base import Base
from app.database.models.audit_mixin import AuditMixin


class Category(Base, AuditMixin):
    __tablename__ = "categories"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )

    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    color = Column(String(7), nullable=False)
    icon = Column(String(100), nullable=False)

    is_active = Column(Boolean, nullable=False, default=True)

    # transactions = relationship(
    #     "Transaction",
    #     secondary="transaction_categories",
    #     back_populates="categories",
    # )

    user_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
    )

    def __init__(
        self,
        name: str,
        color: str,
        icon: str,
        user_id: uuid.UUID,
        description: str | None = None,
        is_active: bool = True,
    ):
        self.name = name
        self.description = description
        self.color = color
        self.icon = icon
        self.is_active = is_active
        self.user_id = user_id