import requests
import os

RESERVATIONS_MICROSERVICE_URL = os.getenv("RESERVATIONS_MICROSERVICE_URL")

def get_reservation(reservation_id):
    """Queries the reservation microservice using GraphQL."""
    query = """
    query GetReservation($id: Int!) {
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
    variables = {"id": int(reservation_id)}

    response = requests.post(
        RESERVATIONS_MICROSERVICE_URL,
        json={"query": query, "variables": variables},
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        result = response.json()
        if "errors" in result:
            raise Exception(f"GraphQL query error: {result['errors']}")
        return result["data"]["getReservationById"]
    else:
        raise Exception(f"Error retrieving reservation {reservation_id}: {response.text}")
