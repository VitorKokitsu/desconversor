from fastapi import FastAPI

from presenter.controllers.conversor import router as conversor
from presenter.controllers.healthcheck import router as healthcheck

app = FastAPI()

app.include_router(healthcheck)
app.include_router(conversor)
