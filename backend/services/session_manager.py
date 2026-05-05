SESSIONS = {}

def crear_sesion(nombre):
    SESSIONS[nombre] = {
        "estado": {},
        "usuarios": []
    }

def unir_usuario(sesion, user):
    SESSIONS[sesion]["usuarios"].append(user)

def obtener_estado(sesion):
    return SESSIONS[sesion]["estado"]

def actualizar_estado(sesion, data):
    SESSIONS[sesion]["estado"].update(data)
