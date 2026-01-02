from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4

from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import (
    CentroTreinamentoIn,
    CentroTreinamentoOut,
)
from workout_api.centro_treinamento.utils import CentroTreinamentoUtils
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter(
    prefix="/centros_treinamento",
    tags=["Centros de Treinamento"],
)


@router.get(
    "/",
    summary="Obter todos os centros de treinamento",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def get_all(
    db_session: DatabaseDependency,
) -> list[CentroTreinamentoOut]:
    return await CentroTreinamentoUtils.filter_all(db_session)


@router.get(
    "/{ct_id}",
    summary="Obter um centro de treinamento específico",
    response_model=CentroTreinamentoOut,
)
async def get_by_id(
    db_session: DatabaseDependency,
    ct_id: UUID4,
) -> CentroTreinamentoOut:
    ct: CentroTreinamentoOut = await CentroTreinamentoUtils.filter_by_id(
        db_session, ct_id
    )

    if not ct:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Centro de Treinamento não encontrado no id: {ct_id}",
        )

    return ct


@router.post(
    "/",
    summary="Criar novo centro de treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency,
    ct_in: CentroTreinamentoIn = Body(...),
) -> CentroTreinamentoOut:
    ct_out = CentroTreinamentoOut(
        id=uuid4(), criado_em=datetime.now(), **ct_in.model_dump()
    )
    ct_model = CentroTreinamentoModel(**ct_out.model_dump())

    db_session.add(ct_model)
    await db_session.commit()

    return ct_out


@router.put(
    "/{ct_id}",
    summary="Atualizar um centro de treinamento existente",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def put(
    db_session: DatabaseDependency,
    ct_id: UUID4,
    ct_in: CentroTreinamentoIn = Body(...),
):
    ct: CentroTreinamentoOut = await CentroTreinamentoUtils.filter_by_id(
        db_session, ct_id
    )

    if not ct:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Centro de Treinamento não encontrado no id: {ct_id}",
        )

    for field, value in ct_in.model_dump().items():
        setattr(ct, field, value)

    db_session.refresh(ct)
    await db_session.commit()

    return CentroTreinamentoOut.model_validate(ct)


@router.delete(
    "/{ct_id}",
    summary="Excluir um centro de treinamento existente",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    db_session: DatabaseDependency,
    ct_id: UUID4,
):
    ct: CentroTreinamentoOut = await CentroTreinamentoUtils.filter_by_id(
        db_session, ct_id
    )

    if not ct:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Centro de Treinamento não encontrado no id: {ct_id}",
        )

    await db_session.delete(ct)
    await db_session.commit()
