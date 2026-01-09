from fastapi import APIRouter, status

from src.configs.dependencies import Database
from src.exceptions import NotFoundError
from src.schemas.auth import LoginIn, LoginOut
from src.security import create_token
from src.services.account import AccountService

router = APIRouter(prefix="/auth", tags=["Auth"])
account_service = AccountService()


@router.post(
    "/login",
    summary="Criar token e efetuar o login.",
    status_code=status.HTTP_200_OK,
    response_model=LoginOut,
)
async def login(db: Database, data: LoginIn):
    user_id = data.user_id
    user = await account_service.read_by(db, user_id=user_id)

    if not user:
        raise NotFoundError("User")

    return create_token(user_id)
