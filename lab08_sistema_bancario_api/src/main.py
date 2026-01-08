from fastapi import FastAPI

from src.routers import routers

app = FastAPI(
    title="DIO Bank API",
    version="0.1.0",
)

for router in routers:
    app.include_router(router)
