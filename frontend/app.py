import streamlit as st
from streamlit_autorefresh import st_autorefresh

from api_client import get_estado, update, evento

# UI
st.set_page_config(layout="wide")
st.title("🏗️ MENFA Plataforma Profesional")

# REFRESH
st_autorefresh(interval=2000, key="sync")

# DATA
piz = get_estado()

# SIDEBAR
st.sidebar.title("Control")

wob = st.sidebar.slider("WOB", 0, 50, piz.get("wob", 10))
rpm = st.sidebar.slider("RPM", 0, 200, piz.get("rpm", 100))
presion = st.sidebar.slider("Presión", 0, 2000, piz.get("presion", 1000))

if st.sidebar.button("Actualizar"):
    update({
        "wob": wob,
        "rpm": rpm,
        "presion": presion
    })

if st.sidebar.button("Forzar Kick"):
    evento("kick")

# DASHBOARD
col1, col2, col3 = st.columns(3)

col1.metric("ROP", round(piz.get("rop", 0), 2))
col2.metric("HHP", round(piz.get("hhp", 0), 2))
col3.metric("Torque", round(piz.get("torque", 0), 2))

st.subheader("Eventos activos")
st.write(piz.get("eventos", []))
if "token" not in st.session_state:
    user = st.text_input("Usuario")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        res = login(user, pwd)
        st.session_state.token = res["token"]
        st.session_state.rol = res["rol"]
        st.rerun()
st.subheader("🛢️ Panel de Control")

col1, col2, col3, col4 = st.columns(4)

col1.metric("ROP", piz["rop"])
col2.metric("HHP", piz["hhp"])
col3.metric("Torque", piz["torque"])
col4.metric("Presión", piz["presion"])

if "alerta" in piz:
    st.error(piz["alerta"])


import streamlit as st
from streamlit_autorefresh import st_autorefresh
from api_client import get_estado, update

st.set_page_config(layout="wide")
st.title("🏗️ MENFA Simulador")

st_autorefresh(interval=2000, key="sync")

piz = get_estado()

st.sidebar.title("Control")

wob = st.sidebar.slider("WOB", 0, 50, piz.get("wob", 10))
rpm = st.sidebar.slider("RPM", 0, 200, piz.get("rpm", 100))
presion = st.sidebar.slider("Presión", 0, 2000, piz.get("presion", 1000))

if st.sidebar.button("Actualizar"):
    update({
        "wob": wob,
        "rpm": rpm,
        "presion": presion
    })

col1, col2, col3 = st.columns(3)

col1.metric("ROP", round(piz.get("rop", 0), 2))
col2.metric("HHP", round(piz.get("hhp", 0), 2))
col3.metric("Torque", round(piz.get("torque", 0), 2))

st.subheader("Eventos")
st.write(piz.get("eventos", []))
