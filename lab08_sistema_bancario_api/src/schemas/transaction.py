from datetime import datetime
from enum import Enum

from pydantic import PositiveFloat

from src.schemas.base import BaseSchema


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class TransationBase(BaseSchema):
    account_id: int
    amount: PositiveFloat


class TransactionIn(TransationBase):
    type: TransactionType

    class Config:
        use_enum_values = True


class TransactionOut(TransationBase):
    id: int
    type: str
    timestamp: datetime
