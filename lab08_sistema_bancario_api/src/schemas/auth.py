from src.schemas.base import BaseSchema


class LoginIn(BaseSchema):
    user_id: int


class LoginOut(BaseSchema):
    access_token: str
