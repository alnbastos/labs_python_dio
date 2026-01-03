from sqlalchemy.future import select

from workout_api.categoria.models import CategoriaModel
from workout_api.categoria.schemas import CategoriaOut
from workout_api.contrib.dependencies import DatabaseDependency


class CategoriaUtils:
    @staticmethod
    async def filter_by(
        db_session: DatabaseDependency,
        **kwargs,
    ) -> CategoriaOut | None:
        stmt = select(CategoriaModel).filter_by(**kwargs)
        result = await db_session.execute(stmt)
        return result.scalars().first()

    @staticmethod
    async def filter_all(db_session: DatabaseDependency) -> list[CategoriaOut]:
        stmt = select(CategoriaModel)
        result = await db_session.execute(stmt)
        return result.scalars().all()
