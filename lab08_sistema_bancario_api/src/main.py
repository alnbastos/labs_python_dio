from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.exceptions import AccountNotFoundError, BusinessError
from src.routers import routers

app = FastAPI(
    title="DIO Bank API",
    version="0.1.0",
)

for router in routers:
    app.include_router(router)


@app.exception_handler(AccountNotFoundError)
async def account_not_found_error_handler(
    request: Request,
    exc: AccountNotFoundError,
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Account not found."},
    )


@app.exception_handler(BusinessError)
async def business_error_handler(request: Request, exc: BusinessError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)}
    )
