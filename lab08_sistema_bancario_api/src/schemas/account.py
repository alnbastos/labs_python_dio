from datetime import datetime

from pydantic import PositiveFloat

from src.schemas.base import BaseSchema


class AccountBase(BaseSchema):
    user_id: int
    balance: PositiveFloat


class AccountIn(AccountBase):
    pass


class AccountOut(AccountBase):
    id: int
    created_at: datetime
