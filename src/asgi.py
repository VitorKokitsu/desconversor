from fastapi import FastAPI

from presenter.controllers.conversor import router as conversor

app = FastAPI()

app.include_router(conversor)
