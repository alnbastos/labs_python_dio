from sqlalchemy.future import select

from src.configs.dependencies import DatabaseDependency
from src.models.account import AccountModel
from src.schemas.account import AccountIn


class AccountService:
    async def read(self, db: DatabaseDependency) -> list[AccountModel]:
        stmt = select(AccountModel)
        result = await db.execute(stmt)
        return result.scalars().all()

    async def create(
        self,
        db: DatabaseDependency,
        account_in: AccountIn,
    ) -> AccountModel:
        account = AccountModel(**account_in.model_dump())
        db.add(account)
        await db.commit()

        return account
