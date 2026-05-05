import requests

def crear_pago(monto, descripcion):
    return {
        "link": f"https://fake.mercadopago/{monto}"
    }
