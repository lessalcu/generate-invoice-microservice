import requests
from datetime import datetime
from app.database.mongo_connection import get_mongo_client
from app.models.invoice import Invoice
import os

# URLs de los microservicios desde .env
USERS_MICROSERVICE_URL = os.getenv("USERS_MICROSERVICE_URL")
RESERVATIONS_MICROSERVICE_URL = os.getenv("RESERVATIONS_MICROSERVICE_URL")

def consultar_usuario(user_id):
    """Consulta al microservicio de usuarios."""
    response = requests.get(f"{USERS_MICROSERVICE_URL}/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al consultar usuario {user_id}: {response.text}")

def consultar_reserva(reserva_id):
    """Consulta al microservicio de reservas utilizando GraphQL."""
    query = """
    query ObtenerReserva($id: Int!) {
        getReservationById(id: $id) {
            id
            userId
            vehicleId
            parkingLotId
            startDate
            endDate
            status
            totalAmount
        }
    }
    """
    variables = {"id": int(reserva_id)}

    response = requests.post(
        RESERVATIONS_MICROSERVICE_URL,
        json={"query": query, "variables": variables},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        result = response.json()
        if "errors" in result:
            raise Exception(f"Error en la consulta GraphQL: {result['errors']}")
        return result["data"]["getReservationById"]
    else:
        raise Exception(f"Error al consultar reserva {reserva_id}: {response.text}")

def generar_factura(reserva_id):
    """Genera una factura basada en la reserva y el usuario relacionado."""
    # Consultar los datos de la reserva
    reserva = consultar_reserva(reserva_id)
    print("Respuesta de la reserva:", reserva)  # Para depurar y verificar el formato de la respuesta
    
    # Verificar que la reserva contiene el campo userId
    if "userId" not in reserva:
        raise Exception(f"La reserva no contiene el campo 'userId': {reserva}")
    
    # Consultar los datos del usuario asociado a la reserva
    usuario = consultar_usuario(reserva["userId"])

    # Crear la factura
    factura = Invoice(
    reserva_id=reserva_id,
    monto_total=reserva["totalAmount"],
    fecha=datetime.utcnow(),
    reserva=reserva,  # Guardar toda la información de la reserva
    usuario=usuario   # Guardar toda la información del usuario
)
    
    # Guardar en MongoDB
    collection = get_mongo_client()
    factura_id = collection.insert_one(factura.to_dict()).inserted_id

    # Respuesta con los datos generados
    return {
        "factura_id": str(factura_id),
        "reserva": reserva,
        "usuario": usuario,
        "monto_total": reserva["totalAmount"],
        "fecha": factura.fecha
    }
