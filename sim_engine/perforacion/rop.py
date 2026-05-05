def calcular_rop(state):
    wob = state.get("wob", 0)
    rpm = state.get("rpm", 0)
    formacion = state.get("formacion", 1)

    if formacion == 0:
        formacion = 1

    return (wob * rpm) / (formacion * 100)
