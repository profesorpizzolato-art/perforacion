from fastapi import FastAPI
from backend.routes import simulacion

app = FastAPI(title="MENFA API")

app.include_router(simulacion.router)
from fastapi import WebSocket
from backend.realtime.ws import connect

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await connect(ws)
