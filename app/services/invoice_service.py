from datetime import datetime, timezone
from app.database.mongo_connection import get_mongo_client
from app.models.invoice import Invoice
from app.services.user_service import consultar_usuario
from app.services.reservation_service import consultar_reserva
from bson import ObjectId  # Importar para manejar ObjectId

def generar_factura(reserva_id):
    """Genera una factura basada en la reserva y el usuario relacionado."""
    
    reserva = consultar_reserva(reserva_id)
    print("Respuesta de la reserva:", reserva)  
    
    if "userId" not in reserva:
        raise Exception(f"La reserva no contiene el campo 'userId': {reserva}")
    
    usuario = consultar_usuario(reserva["userId"])

    # Crear el documento de la factura incluyendo reserva y usuario
    factura_data = {
        "reserva_id": reserva_id,
        "monto_total": reserva["totalAmount"],
        "fecha": datetime.now(timezone.utc),
        "reserva": reserva,
        "usuario": usuario
    }

    collection = get_mongo_client()
    factura_id = collection.insert_one(factura_data).inserted_id  # Guardar en MongoDB

    # Convertir a string todos los ObjectId en la respuesta
    def serialize_mongo_data(data):
        if isinstance(data, ObjectId):
            return str(data)
        elif isinstance(data, dict):
            return {k: serialize_mongo_data(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [serialize_mongo_data(item) for item in data]
        return data

    return serialize_mongo_data({
        "factura_id": factura_id,
        **factura_data
    })
