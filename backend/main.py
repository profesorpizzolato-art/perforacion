from fastapi import FastAPI, WebSocket
from backend.routes import simulacion
from backend.realtime.ws import connect
from sim_engine.engine import run_simulation

app = FastAPI(title="MENFA API")

# -------------------------
# ESTADO GLOBAL
# -------------------------
STATE = {
    "wob": 10,
    "rpm": 100,
    "presion": 1000,
    "caudal": 500,
    "profundidad_actual": 1000,
    "formacion": 1,
    "alarma": False,
    "mensaje": "Sistema OK"
}

# -------------------------
# ROUTERS
# -------------------------
app.include_router(simulacion.router)

# -------------------------
# ENDPOINTS
# -------------------------
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

# -------------------------
# WEBSOCKET
# -------------------------
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await connect(ws)
