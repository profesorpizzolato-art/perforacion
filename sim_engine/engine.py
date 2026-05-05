from sim_engine.perforacion.rop import calcular_rop
from sim_engine.perforacion.hidraulica import calcular_hhp
from sim_engine.torque_drag.torque import calcular_torque
from sim_engine.geonavegacion.trayectoria import calcular_trayectoria
from sim_engine.eventos.event_manager import evaluar_eventos
from sim_engine.control_pozos.kick import detectar_kick

if detectar_kick(state):
    resultado["alerta"] = "KICK DETECTADO"
def run_simulation(state):
    resultado = {}

    # 🛢️ PERFORACIÓN
    resultado["rop"] = calcular_rop(state)
    resultado["hhp"] = calcular_hhp(state)

    # 🔩 TORQUE & DRAG
    resultado["torque"] = calcular_torque(state)

    # 🧭 GEO
    resultado["trayectoria"] = calcular_trayectoria(state)

    # ⚠️ EVENTOS
    eventos = evaluar_eventos(state)
    resultado["eventos"] = eventos

    return resultado
