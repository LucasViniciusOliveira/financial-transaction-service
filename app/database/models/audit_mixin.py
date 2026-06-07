from sqlalchemy import (
    Column,
    DateTime,
    func,
)


class AuditMixin:
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    deleted_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )