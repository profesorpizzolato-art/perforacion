def detectar_kick(state):
    if state["presion"] < state["presion_formacion"]:
        return True
    return False
