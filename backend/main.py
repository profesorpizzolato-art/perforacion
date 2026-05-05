from fastapi import FastAPI
from backend.routes import simulacion

app = FastAPI(title="MENFA API")

app.include_router(simulacion.router)
from fastapi import WebSocket
from backend.realtime.ws import connect

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await connect(ws)

from fastapi import FastAPI
from sim_engine.engine import run_simulation

app = FastAPI()

STATE = {
    "wob": 10,
    "rpm": 100,
    "presion": 1000,
    "caudal": 500,
    "profundidad_actual": 1000,
    "formacion": 1
}

@app.get("/")
def root():
    return {"status": "MENFA API OK"}

@app.get("/estado")
def estado():
    sim = run_simulation(STATE)
    return {**STATE, **sim}

@app.post("/control")
def control(data: dict):
    STATE.update(data)
    return {"ok": True}
