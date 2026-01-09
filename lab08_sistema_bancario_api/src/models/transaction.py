from datetime import datetime
from decimal import Decimal
from enum import Enum

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import BaseModel


class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class TransactionModel(BaseModel):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(
        sa.BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    account_id: Mapped[int] = mapped_column(
        sa.Integer,
        sa.ForeignKey("accounts.id"),
        nullable=False,
    )
    amount: Mapped[Decimal] = mapped_column(
        sa.Numeric(10, 2),
        nullable=False,
        server_default=sa.text("0"),
    )
    type: Mapped[TransactionType] = mapped_column(
        sa.Enum(TransactionType, name="transaction_types"),
        nullable=False,
    )
    timestamp: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(timezone=True),  # TIMESTAMPTZ
        nullable=False,
        server_default=sa.func.now(),
    )
