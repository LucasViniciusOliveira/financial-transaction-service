from enum import Enum


class TransactionStatusEnum(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"


class TransactionTypeEnum(str, Enum):
    EXPENSE = "EXPENSE"
    INCOME = "INCOME"
    TRANSFER = "TRANSFER"


class PaymentMethodEnum(str, Enum):
    CARD = "CARD"
    PIX = "PIX"
    CASH = "CASH"
    TRANSFER = "TRANSFER"


class CardTypeEnum(str, Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    FOOD = "FOOD"


class RecurrenceFrequencyEnum(str, Enum):
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"