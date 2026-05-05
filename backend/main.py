from fastapi import FastAPI
from backend.routes import simulacion

app = FastAPI(title="MENFA API")

app.include_router(simulacion.router)
