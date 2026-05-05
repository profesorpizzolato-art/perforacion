from fastapi import WebSocket

connections = []

async def connect(ws: WebSocket):
    await ws.accept()
    connections.append(ws)

async def broadcast(data: dict):
    for conn in connections:
        await conn.send_json(data)
