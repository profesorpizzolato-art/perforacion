from fastapi import APIRouter

router = APIRouter()

CURSOS = [
    {"id": 1, "nombre": "Control de Pozos"},
    {"id": 2, "nombre": "Perforación"}
]

@router.get("/cursos")
def get_cursos():
    return CURSOS
