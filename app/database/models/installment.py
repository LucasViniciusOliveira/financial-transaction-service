import uuid

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.dialects.postgresql import UUID

from app.database.base import Base
from app.database.models.audit_mixin import AuditMixin


class Installment(Base, AuditMixin):
    __tablename__ = "installments"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )

    number = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)

    amount = Column(
        Numeric(10, 2),
        nullable=False,
    )


    def __init__(
        self,
        number: int,
        total: int,
        amount: float,
    ):
        self.number = number
        self.total = total
        self.amount = amount