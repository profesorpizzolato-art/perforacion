def blowout(state):
    state["presion"] -= 800
    state["caudal"] += 300
    state["alarma"] = True
    return state
