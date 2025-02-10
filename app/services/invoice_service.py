from datetime import datetime, timezone
from app.database.mongo_connection import get_mongo_client
from app.models.invoice import Invoice
from app.services.user_service import get_user
from app.services.reservation_service import get_reservation
from bson import ObjectId  # Import to handle ObjectId

def generate_invoice(reservation_id):
    """Generates an invoice based on the reservation and related user."""
    
    reservation = get_reservation(reservation_id)
    print("Reservation response:", reservation)  
    
    if "userId" not in reservation:
        raise Exception(f"Reservation does not contain 'userId' field: {reservation}")
    
    user = get_user(reservation["userId"])

    # Create the invoice document including reservation and user
    invoice_data = {
        "reservation_id": reservation_id,
        "total_amount": reservation["totalAmount"],
        "date": datetime.now(timezone.utc),
        "reservation": reservation,
        "user": user
    }

    collection = get_mongo_client()
    invoice_id = collection.insert_one(invoice_data).inserted_id  # Save to MongoDB

    # Convert all ObjectId fields to string
    def serialize_mongo_data(data):
        if isinstance(data, ObjectId):
            return str(data)
        elif isinstance(data, dict):
            return {k: serialize_mongo_data(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [serialize_mongo_data(item) for item in data]
        return data

    return serialize_mongo_data({
        "invoice_id": invoice_id,
        **invoice_data
    })
