import requests

API = "https://TU-BACKEND"

def login(username, password):
    res = requests.post(f"{API}/login", json={
        "username": username,
        "password": password
    })
    return res.json()
