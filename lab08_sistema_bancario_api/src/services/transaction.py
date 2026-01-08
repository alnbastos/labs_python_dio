from sqlalchemy.future import select

from src.configs.dependencies import DatabaseDependency
from src.exceptions import AccountNotFoundError, BusinessError
from src.models.account import AccountModel
from src.models.transaction import TransactionModel, TransactionType
from src.schemas.transaction import TransactionIn
from src.services.account import AccountService


class TransactionService:
    account_service = AccountService()

    async def read(self, db: DatabaseDependency) -> list[TransactionModel]:
        stmt = select(TransactionModel)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def create(
        self,
        db: DatabaseDependency,
        transaction: TransactionIn,
    ) -> TransactionModel:

        # Obtem a conta bancária
        account = await self.account_service.read_by_id(
            db=db, pk=transaction.account_id
        )
        if not account:
            raise AccountNotFoundError

        tr = TransationRepository(
            balance=float(account.balance),
            amount=float(transaction.amount),
        )
        if transaction.type == TransactionType.WITHDRAWAL:
            balance = tr.withdrawal()
        else:
            balance = tr.deposit()

        # Registra os dados da transação
        t = await self.__register_transaction(db, transaction)

        # Atualiza o valor do saldo na conta bancária, após a transferência
        await self.__update_account_balance(db, account, balance)

        return t

    async def __update_account_balance(
        self,
        db,
        account: AccountModel,
        balance: float,
    ) -> None:
        account.balance = balance
        await db.commit()
        await db.refresh(account)

    async def __register_transaction(
        self,
        db: DatabaseDependency,
        transaction: TransactionIn,
    ) -> TransactionModel:
        model = TransactionModel(**transaction.model_dump())
        db.add(model)
        await db.commit()
        return model


class TransationRepository:
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount

    def withdrawal(self):
        balance = float(self.balance) - self.amount

        if balance < 0:
            msg = "Operation not carried out due to lack of balance"
            raise BusinessError(msg)

        return balance

    def deposit(self):
        return float(self.balance) + self.amount
