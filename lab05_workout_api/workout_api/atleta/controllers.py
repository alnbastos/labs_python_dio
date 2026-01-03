from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.exc import IntegrityError

from workout_api.atleta.models import AtletaModel
from workout_api.atleta.schemas import AtletaIn, AtletaOut
from workout_api.atleta.utils import AtletaUtils
from workout_api.categoria.utils import CategoriaUtils
from workout_api.centro_treinamento.utils import CentroTreinamentoUtils
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter(prefix="/atletas", tags=["Atletas"])


@router.get(
    "/",
    summary="Obter todos os atletas",
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaOut],
)
async def get_all(db_session: DatabaseDependency) -> list[AtletaOut]:
    atletas = await AtletaUtils.filter_all(db_session)
    return [AtletaOut.model_validate(atleta) for atleta in atletas]


@router.get(
    "/{atleta_id}",
    summary="Obter um atleta específico",
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def get_by_id(
    db_session: DatabaseDependency,
    atleta_id: UUID4,
) -> AtletaOut:
    atleta: AtletaOut = await AtletaUtils.filter_by_id(db_session, atleta_id)

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrado no id: {atleta_id}",
        )

    return atleta


@router.post(
    "/",
    summary="Criar novo atleta",
    status_code=status.HTTP_201_CREATED,
)
async def post(
    db_session: DatabaseDependency,
    atleta_in: AtletaIn = Body(...),
) -> AtletaOut:
    categoria_atleta: str = atleta_in.categoria.nome
    ct_atleta = atleta_in.centro_treinamento.nome

    categoria = await CategoriaUtils.filter_by(
        db_session, nome=categoria_atleta
    )
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria não encontrada com o nome: {categoria_atleta}",
        )

    ct = await CentroTreinamentoUtils.filter_by(
        db_session, nome=ct_atleta
    )
    if not ct:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de Treinamento não encontrado "
                   f"com o nome: {ct_atleta}",
        )

    try:
        atleta_out = AtletaOut(
            id=uuid4(), criado_em=datetime.now(), **atleta_in.model_dump()
        )
        atleta_model = AtletaModel(
            **atleta_out.model_dump(
                exclude=["categoria", "centro_treinamento"]
            )
        )
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = ct.pk_id

        db_session.add(atleta_model)
        await db_session.commit()

    except IntegrityError as ie:
        if "atletas_cpf_key" in str(ie.orig):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe um atleta cadastrado com este CPF.",
            )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro de integridade ao inserir os dados do atleta.",
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocorreu um erro ao inserir os dados no banco.",
        )

    return atleta_out


@router.put(
    "/{atleta_id}",
    summary="Atualizar um atleta existente",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def put(
    db_session: DatabaseDependency,
    atleta_id: UUID4,
    atleta_in: AtletaIn = Body(...),
):
    atleta: AtletaOut = await AtletaUtils.filter_by_id(db_session, atleta_id)

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrado no id: {atleta_id}",
        )

    data = atleta_in.model_dump(exclude_unset=True)

    for field in ["nome", "idade", "peso", "altura", "sexo"]:
        if field in data:
            setattr(atleta, field, data[field])

    if "categoria_id" in data:
        atleta.categoria_id = data["categoria_id"]

    if "centro_treinamento_id" in data:
        atleta.centro_treinamento_id = data["centro_treinamento_id"]

    await db_session.commit()
    await db_session.refresh(atleta)

    return AtletaOut.model_validate(atleta)


@router.delete(
    "/{atleta_id}",
    summary="Excluir um atleta existente",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    db_session: DatabaseDependency,
    atleta_id: UUID4,
):
    atleta: AtletaModel = await AtletaUtils.filter_by_id(db_session, atleta_id)
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Atleta não encontrado no id: {atleta_id}",
        )

    await db_session.delete(atleta)
    await db_session.commit()
