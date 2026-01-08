from fastapi import APIRouter, status

from src.configs.dependencies import DatabaseDependency
from src.schemas.transaction import TransactionIn, TransactionOut
from src.services.transaction import TransactionService

router = APIRouter(prefix="/transactions", tags=["Transactions"])
service = TransactionService()


@router.post(
    "/",
    summary="Criar/Efetuar uma transação bancária.",
    status_code=status.HTTP_201_CREATED,
    response_model=TransactionOut,
)
async def create(db: DatabaseDependency, transaction_in: TransactionIn):
    transaction = await service.create(db, transaction_in)
    return TransactionOut.model_validate(transaction)
