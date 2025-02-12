import requests
import os

RESERVATIONS_MICROSERVICE_URL = os.getenv("RESERVATIONS_MICROSERVICE_URL", "http://75.101.158.182:4003/reservation")

def get_reservation(reservation_id):
    """Queries the reservation microservice using GraphQL without variables."""
    query = f"""
    {{
        getReservationById(id: {reservation_id}) {{
            id
            userId
            vehicleId
            parkingLotId
            startDate
            endDate
            status
            totalAmount
        }}
    }}
    """

    response = requests.post(
        RESERVATIONS_MICROSERVICE_URL,
        json={"query": query},
        headers={"Content-Type": "application/json"}
    )

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")

    if response.status_code == 200:
        result = response.json()
        if "errors" in result:
            raise Exception(f"GraphQL query error: {result['errors']}")
        return result["data"]["getReservationById"]
    else:
        raise Exception(f"Error retrieving reservation {reservation_id}: {response.text}")

# Test
reservation = get_reservation(2)
print(reservation)
