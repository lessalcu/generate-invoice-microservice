import requests
import os

RESERVATIONS_MICROSERVICE_URL = os.getenv("RESERVATIONS_MICROSERVICE_URL")

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
