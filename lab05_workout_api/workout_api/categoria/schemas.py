from typing import Annotated

from pydantic import Field

from workout_api.contrib.schemas import BaseSchema, OutMixin


class Categoria(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome da Categoria",
            example="Scale",
            max_length=10,
        ),
    ]


class CategoriaIn(Categoria):
    pass


class CategoriaOut(Categoria, OutMixin):
    pass
