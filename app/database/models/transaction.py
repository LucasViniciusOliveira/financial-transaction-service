import uuid

from datetime import datetime, date
from decimal import Decimal
from uuid import UUID, uuid4

from sqlalchemy import (
    Column,
    String,
    DateTime,
    Numeric,
    ForeignKey,
    Enum as SqlEnum,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.base import Base

from app.database.models.audit_mixin import AuditMixin
from app.enums.transaction import (
    TransactionStatusEnum,
    TransactionTypeEnum,
    PaymentMethodEnum,
    CardTypeEnum,
)


class Transaction(Base, AuditMixin):
    __tablename__ = "transactions"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        nullable=False,
    )

    parent_transaction_id = Column(
        UUID(as_uuid=True),
        ForeignKey("transactions.id"),
        nullable=True,
    )

    identification = Column(
        String(255),
        nullable=False,
    )

    description = Column(
        String,
        nullable=True,
    )

    status = Column(
        SqlEnum(TransactionStatusEnum),
        nullable=False,
        default=TransactionStatusEnum.PENDING,
    )

    type = Column(
        SqlEnum(TransactionTypeEnum),
        nullable=False,
    )

    payment_method = Column(
        SqlEnum(PaymentMethodEnum),
        nullable=False,
    )

    card_type = Column(
        SqlEnum(CardTypeEnum),
        nullable=True,
    )

    due_date = Column(
        DateTime,
        nullable=True,
    )

    payment_date = Column(
        DateTime,
        nullable=True,
    )

    amount = Column(
        Numeric(10, 2),
        nullable=False,
    )

    payment_receipt_url = Column(
        String,
        nullable=True,
    )

    card_id = Column(
        String(255),
        nullable=True,
    )

    bank_account_output_id = Column(
        String(255),
        nullable=True,
    )

    bank_account_input_id = Column(
        String(255),
        nullable=True,
    )

    installment_id = Column(
        UUID(as_uuid=True),
        ForeignKey("installments.id"),
        nullable=True,
    )

    recurrence_rule_id = Column(
        UUID(as_uuid=True),
        ForeignKey("recurrence_rules.id"),
        nullable=True,
    )

    user_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        index=True,
    )

    installment = relationship(
        "Installment",
        foreign_keys=[installment_id],
    )

    recurrence_rule = relationship(
        "RecurrenceRule",
        foreign_keys=[recurrence_rule_id],
    )

    parent_transaction = relationship(
        "Transaction",
        remote_side=[id],
    )

    categories = relationship(
        "Category",
        secondary="transaction_categories",
        back_populates="transactions",
    )

    def __init__(
        self,
        identification: str,
        type: TransactionTypeEnum,
        payment_method: PaymentMethodEnum,
        amount: Decimal,
        user_id: uuid.UUID,

        description: str = None,
        parent_transaction_id: UUID = None,

        status: TransactionStatusEnum = TransactionStatusEnum.PENDING,

        card_type: CardTypeEnum = None,

        due_date: datetime = None,
        payment_date: datetime = None,

        payment_receipt_url: str = None,

        card_id: str = None,

        bank_account_output_id: str = None,
        bank_account_input_id: str = None,

        installment_id: UUID = None,
        recurrence_rule_id: UUID = None,

        categories: list = None,
    ):
        # =========================
        # REGRAS DE NEGÓCIO
        # =========================

        if amount <= 0:
            raise ValueError("amount must be greater than zero")

        if payment_method == PaymentMethodEnum.CARD:
            if not card_type:
                raise ValueError(
                    "card_type is required for CARD payments"
                )

            if not card_id:
                raise ValueError(
                    "card_id is required for CARD payments"
                )

        if type == TransactionTypeEnum.EXPENSE:
            if not bank_account_output_id:
                raise ValueError(
                    "bank_account_output_id is required for EXPENSE transactions"
                )

        if type == TransactionTypeEnum.INCOME:
            if not bank_account_input_id:
                raise ValueError(
                    "bank_account_input_id is required for INCOME transactions"
                )

        # =========================
        # ATRIBUIÇÃO
        # =========================

        self.parent_transaction_id = parent_transaction_id

        self.identification = identification
        self.description = description

        self.status = status
        self.type = type

        self.payment_method = payment_method
        self.card_type = card_type

        self.due_date = due_date
        self.payment_date = payment_date

        self.amount = amount

        self.payment_receipt_url = payment_receipt_url

        self.card_id = card_id

        self.bank_account_output_id = bank_account_output_id
        self.bank_account_input_id = bank_account_input_id

        self.installment_id = installment_id
        self.recurrence_rule_id = recurrence_rule_id
        self.user_id = user_id
        self.categories = categories or []
