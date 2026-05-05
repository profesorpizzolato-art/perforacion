from fastapi import APIRouter
from sim_engine.engine import run_simulation

router = APIRouter()

# Estado global simple (luego lo pasamos a DB)
STATE = {
    "wob": 10,
    "rpm": 100,
    "presion": 1000,
    "caudal": 500,
    "profundidad_actual": 1000,
    "formacion": 1
}

@router.get("/estado")
def get_estado():
    sim = run_simulation(STATE)
    return {**STATE, **sim}

@router.post("/control")
def update_control(data: dict):
    STATE.update(data)
    return {"ok": True}

@router.post("/evento/{tipo}")
def evento(tipo: str):
    if tipo == "kick":
        STATE["presion"] -= 300
    return {"evento": tipo}
