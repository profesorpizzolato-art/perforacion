from fastapi import APIRouter
from sim_engine.eventos.blowout import blowout

router = APIRouter()

STATE = {}

@router.post("/evento/blowout")
def trigger():
    global STATE
    STATE = blowout(STATE)
    return {"evento": "blowout"}
