import requests
import os

USERS_MICROSERVICE_URL = os.getenv("USERS_MICROSERVICE_URL")

def consultar_usuario(user_id):
    """Consulta al microservicio de usuarios."""
    response = requests.get(f"{USERS_MICROSERVICE_URL}/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al consultar usuario {user_id}: {response.text}")
