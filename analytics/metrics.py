def calcular_performance(state):
    score = 0

    if state["eventos"] == []:
        score += 50

    if state["rop"] > 20:
        score += 50

    return score
