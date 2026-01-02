from pydantic import UUID4
from sqlalchemy.future import select

from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import CentroTreinamentoOut
from workout_api.contrib.dependencies import DatabaseDependency


class CentroTreinamentoUtils:
    async def filter_by_id(
        db_session: DatabaseDependency, ct_id: UUID4
    ) -> CentroTreinamentoOut:
        return (
            (
                await db_session.execute(
                    select(CentroTreinamentoModel).filter_by(id=ct_id)
                )
            )
            .scalars()
            .first()
        )

    async def filter_all(
        db_session: DatabaseDependency,
    ) -> list[CentroTreinamentoOut]:
        return (
            (
                await db_session.execute(select(CentroTreinamentoModel))
            )
            .scalars()
            .all()
        )
