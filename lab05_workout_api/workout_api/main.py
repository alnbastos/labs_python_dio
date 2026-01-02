from fastapi import FastAPI

from workout_api.categoria.controllers import router as router_categoria

app = FastAPI(title="Workout API")

routers = [
    router_categoria,
]

for router in routers:
    app.include_router(router)
