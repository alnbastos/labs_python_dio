from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4

from workout_api.categoria.models import CategoriaModel
from workout_api.categoria.schemas import CategoriaIn, CategoriaOut
from workout_api.categoria.utils import CategoriaUtils
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.get(
    "/",
    summary="Obter todas as categorias",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def get_all(db_session: DatabaseDependency) -> list[CategoriaOut]:
    return await CategoriaUtils.filter_all(db_session)


@router.get(
    "/{categoria_id}",
    summary="Obter uma categoria específica",
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def get_by_id(
    db_session: DatabaseDependency, categoria_id: UUID4
) -> CategoriaOut:
    categoria: CategoriaOut = await CategoriaUtils.filter_by(
        db_session, id=categoria_id
    )

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria não encontrada no id: {categoria_id}",
        )

    return categoria


@router.post(
    "/",
    summary="Criar nova categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    db_session: DatabaseDependency,
    categoria_in: CategoriaIn = Body(...),
) -> CategoriaOut:
    categoria_out = CategoriaOut(
        id=uuid4(), criado_em=datetime.now(), **categoria_in.model_dump()
    )
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out


@router.put(
    "/{categoria_id}",
    summary="Atualizar uma categoria existente",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def put(
    db_session: DatabaseDependency,
    categoria_id: UUID4,
    categoria_in: CategoriaIn = Body(...),
):
    categoria: CategoriaOut = await CategoriaUtils.filter_by(
        db_session, id=categoria_id
    )

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria não encontrada no id: {categoria_id}",
        )

    for field, value in categoria_in.model_dump().items():
        setattr(categoria, field, value)

    db_session.refresh(categoria)
    await db_session.commit()

    return CategoriaOut.model_validate(categoria)


@router.delete(
    "/{categoria_id}",
    summary="Excluir uma categoria existente",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    db_session: DatabaseDependency,
    categoria_id: UUID4,
):
    categoria: CategoriaOut = await CategoriaUtils.filter_by(
        db_session, id=categoria_id
    )

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria não encontrada no id: {categoria_id}",
        )

    await db_session.delete(categoria)
    await db_session.commit()
