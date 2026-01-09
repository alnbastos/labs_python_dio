from src.controllers.account import router as account_router
from src.controllers.auth import router as auth_router
from src.controllers.transaction import router as transaction_router

routers = [
    auth_router,
    account_router,
    transaction_router,
]
