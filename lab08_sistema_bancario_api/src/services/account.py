from sqlalchemy.future import select

from src.configs.dependencies import Database
from src.models.account import AccountModel
from src.schemas.account import AccountIn


class AccountService:
    async def read(self, db: Database) -> list[AccountModel]:
        stmt = select(AccountModel)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def read_by_id(self, db: Database, pk: int) -> AccountModel:
        stmt = select(AccountModel).filter_by(id=pk)
        result = await db.execute(stmt)
        return result.scalars().first()

    async def read_by(self, db: Database, **kwargs) -> AccountModel:
        stmt = select(AccountModel).filter_by(**kwargs)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def create(
        self,
        db: Database,
        account_in: AccountIn,
    ) -> AccountModel:
        account = AccountModel(**account_in.model_dump())
        db.add(account)
        await db.commit()

        return account
