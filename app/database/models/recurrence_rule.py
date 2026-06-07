import uuid

from datetime import date
from sqlalchemy import (
    Boolean,
    Column,
    Date,
    Integer,
    Enum,
)
from app.database.base import Base
from app.database.models.audit_mixin import AuditMixin
from app.enums.transaction import RecurrenceFrequencyEnum
from sqlalchemy.dialects.postgresql import UUID

class RecurrenceRule(Base, AuditMixin):
    __tablename__ = "recurrence_rules"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False
    )

    recurrence_frequency = Column(
        Enum(RecurrenceFrequencyEnum),
        nullable=False
    )
    installment_quantity = Column(Integer, nullable=True)

    is_recurring = Column(Boolean, nullable=False, default=False)
    is_installment = Column(Boolean, nullable=False, default=False)

    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    next_execution = Column(Date, nullable=True)

    def __init__(
        self,
        recurrence_frequency: str,
        installment_quantity: int | None = None,
        is_recurring: bool = False,
        is_installment: bool = False,
        start_date: date | None = None,
        end_date: date | None = None,
        next_execution: date | None = None,
    ):
        self.recurrence_frequency = recurrence_frequency
        self.installment_quantity = installment_quantity
        self.is_recurring = is_recurring
        self.is_installment = is_installment
        self.start_date = start_date
        self.end_date = end_date
        self.next_execution = next_execution
