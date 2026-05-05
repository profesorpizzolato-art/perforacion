def evaluar_eventos(state):
    eventos = []

    if state["presion"] < 500:
        eventos.append("kick")

    if state["caudal"] > 800:
        eventos.append("perdida")

    if state["rpm"] > 180:
        eventos.append("vibracion")

    return eventos
