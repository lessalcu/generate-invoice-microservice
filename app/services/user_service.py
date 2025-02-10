import requests
import os

USERS_MICROSERVICE_URL = os.getenv("USERS_MICROSERVICE_URL")

def get_user(user_id):
    """Queries the user microservice."""
    response = requests.get(f"{USERS_MICROSERVICE_URL}/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error retrieving user {user_id}: {response.text}")
