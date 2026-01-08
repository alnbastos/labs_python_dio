from datetime import datetime
from decimal import Decimal

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import BaseModel


class AccountModel(BaseModel):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(
        sa.BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    user_id: Mapped[int] = mapped_column(
        sa.BigInteger,
        nullable=False,
        index=True,
    )

    balance: Mapped[Decimal] = mapped_column(
        sa.Numeric(10, 2),
        nullable=False,
        server_default=sa.text("0"),
    )

    created_at: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(timezone=True),  # TIMESTAMPTZ
        nullable=False,
        server_default=sa.func.now(),
    )
