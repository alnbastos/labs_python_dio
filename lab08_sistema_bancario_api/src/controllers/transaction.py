from fastapi import APIRouter, Depends, status

from src.configs.dependencies import Database
from src.schemas.transaction import TransactionIn, TransactionOut
from src.security import verify_token
from src.services.transaction import TransactionService

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
    dependencies=[Depends(verify_token)],
)
service = TransactionService()


@router.post(
    "/",
    summary="Criar/Efetuar uma transação bancária.",
    status_code=status.HTTP_201_CREATED,
    response_model=TransactionOut,
)
async def create(db: Database, transaction_in: TransactionIn):
    transaction = await service.create(db, transaction_in)
    return TransactionOut.model_validate(transaction)
