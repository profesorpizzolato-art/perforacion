from fastapi import APIRouter
from backend.services.session_manager import *

router = APIRouter()

@router.post("/sesion/crear")
def crear(data: dict):
    crear_sesion(data["nombre"])
    return {"ok": True}

@router.post("/sesion/unir")
def unir(data: dict):
    unir_usuario(data["sesion"], data["usuario"])
    return {"ok": True}

@router.get("/sesion/{nombre}")
def estado(nombre: str):
    return obtener_estado(nombre)
