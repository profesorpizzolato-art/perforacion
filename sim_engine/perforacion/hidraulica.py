def calcular_hhp(state):
    presion = state.get("presion", 0)
    caudal = state.get("caudal", 0)

    return (presion * caudal) / 1714
