import requests

API = "https://TU-BACKEND.onrender.com"

def get_estado():
    return requests.get(f"{API}/estado").json()

def update(data):
    requests.post(f"{API}/control", json=data)

def evento(tipo):
    requests.post(f"{API}/evento/{tipo}")
