from datetime import datetime

from pydantic import UUID4, BaseModel


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True


class OutMixin(BaseSchema):
    id: UUID4
    criado_em: datetime
