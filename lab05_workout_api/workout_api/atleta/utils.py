from pydantic import UUID4
from sqlalchemy.future import select

from workout_api.atleta.models import AtletaModel
from workout_api.atleta.schemas import AtletaOut
from workout_api.contrib.dependencies import DatabaseDependency


class AtletaUtils:
    @staticmethod
    async def filter_by_id(
        db_session: DatabaseDependency, atleta_id: UUID4
    ) -> AtletaOut | None:
        stmt = select(AtletaModel).filter_by(id=atleta_id)
        result = await db_session.execute(stmt)
        return result.scalars().first()

    @staticmethod
    async def filter_all(db_session: DatabaseDependency) -> list[AtletaOut]:
        stmt = select(AtletaModel)
        result = await db_session.execute(stmt)
        return result.scalars().all()
