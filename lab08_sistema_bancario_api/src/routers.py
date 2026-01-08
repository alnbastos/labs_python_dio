from src.controllers.account import router as account_router
from src.controllers.transaction import router as transaction_router

routers = [
    account_router,
    transaction_router,
]
