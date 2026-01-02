from typing import Annotated

from pydantic import Field

from workout_api.contrib.schemas import BaseSchema, OutMixin


class CentroTreinamento(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do Centro de Treinamento",
            example="CT King",
            max_length=20,
        ),
    ]
    endereco: Annotated[
        str,
        Field(
            description="Endereço do Centro de Treinamento",
            example="Rua X. 002",
            max_length=60,
        ),
    ]
    proprietario: Annotated[
        str,
        Field(
            description="Prorietário do Centro de Treinamento",
            example="Marcos",
            max_length=30,
        ),
    ]


class CentroTreinamentoIn(CentroTreinamento):
    pass


class CentroTreinamentoOut(CentroTreinamento, OutMixin):
    pass
