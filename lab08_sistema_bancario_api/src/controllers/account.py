from fastapi import APIRouter, status

from src.configs.dependencies import Database
from src.schemas.account import AccountIn, AccountOut
from src.schemas.transaction import TransactionOut
from src.services.account import AccountService
from src.services.transaction import TransactionService

router = APIRouter(prefix="/accounts", tags=["Accounts"])

account_service = AccountService()
tx_service = TransactionService()


@router.get(
    "/",
    summary="Obter todas as contas bancárias.",
    status_code=status.HTTP_200_OK,
    response_model=list[AccountOut],
)
async def read(db: Database):
    accounts = await account_service.read(db)
    return [AccountOut.model_validate(account) for account in accounts]


@router.get(
    "/{pk}/transactions",
    summary="Criar/Efetuar uma transação bancária.",
    status_code=status.HTTP_200_OK,
    response_model=list[TransactionOut],
)
async def read_account_transactions(db: Database, pk: int):
    transactions = await tx_service.read_by(db=db, account_id=pk)
    return [TransactionOut.model_validate(t) for t in transactions]


@router.post(
    "/",
    summary="Criar uma conta bancária.",
    status_code=status.HTTP_201_CREATED,
    response_model=AccountOut,
)
async def create(db: Database, account_in: AccountIn) -> AccountOut:
    account = await account_service.create(db, account_in)
    return AccountOut.model_validate(account)
