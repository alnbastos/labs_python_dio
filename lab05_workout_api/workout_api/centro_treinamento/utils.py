from sqlalchemy.future import select

from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import CentroTreinamentoOut
from workout_api.contrib.dependencies import DatabaseDependency


class CentroTreinamentoUtils:
    @staticmethod
    async def filter_by(
        db_session: DatabaseDependency,
        **kwargs,
    ) -> CentroTreinamentoOut | None:
        stmt = select(CentroTreinamentoModel).filter_by(**kwargs)
        result = await db_session.execute(stmt)
        return result.scalars().first()

    @staticmethod
    async def filter_all(
        db_session: DatabaseDependency,
    ) -> list[CentroTreinamentoOut]:
        stmt = select(CentroTreinamentoModel)
        result = await db_session.execute(stmt)
        return result.scalars().all()
