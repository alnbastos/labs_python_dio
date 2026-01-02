from fastapi import FastAPI

from workout_api.categoria.controllers import router as router_categoria
from workout_api.centro_treinamento.controllers import (
    router as router_centro_treinamento,
)

app = FastAPI(title="Workout API")

routers = [
    router_categoria,
    router_centro_treinamento,
]

for router in routers:
    app.include_router(router)
