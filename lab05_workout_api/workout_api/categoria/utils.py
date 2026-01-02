from pydantic import UUID4
from sqlalchemy.future import select

from workout_api.categoria.models import CategoriaModel
from workout_api.categoria.schemas import CategoriaOut
from workout_api.contrib.dependencies import DatabaseDependency


class CategoriaUtils:
    async def filter_by_id(
        db_session: DatabaseDependency, categoria_id: UUID4
    ) -> CategoriaOut:
        return (
            (
                await db_session.execute(
                    select(CategoriaModel).filter_by(id=categoria_id)
                )
            )
            .scalars()
            .first()
        )

    async def filter_all(db_session: DatabaseDependency) -> list[CategoriaOut]:
        return (await db_session.execute(select(CategoriaModel))).scalars().all()
