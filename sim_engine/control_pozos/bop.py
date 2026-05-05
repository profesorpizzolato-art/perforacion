def cerrar_bop(state):
    state["bop"] = "cerrado"
    state["caudal"] = 0
    return state
