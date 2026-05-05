from fastapi import APIRouter
from backend.auth.security import create_token

router = APIRouter()

USERS = {
    "instructor": {"password": "1234", "rol": "instructor"},
    "alumno": {"password": "1234", "rol": "alumno"}
}

@router.post("/login")
def login(data: dict):
    user = USERS.get(data["username"])

    if not user or user["password"] != data["password"]:
        return {"error": "credenciales invalidas"}

    token = create_token({
        "user": data["username"],
        "rol": user["rol"]
    })

    return {"token": token, "rol": user["rol"]}
