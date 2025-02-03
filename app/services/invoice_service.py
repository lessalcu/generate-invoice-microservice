from datetime import datetime
from app.database.mongo_connection import get_mongo_client
from app.models.invoice import Invoice
from services.user_service import consultar_usuario
from services.reservation_service import consultar_reserva

def generar_factura(reserva_id):
    """Genera una factura basada en la reserva y el usuario relacionado."""
    
    reserva = consultar_reserva(reserva_id)
    print("Respuesta de la reserva:", reserva)  
    
    if "userId" not in reserva:
        raise Exception(f"La reserva no contiene el campo 'userId': {reserva}")
    
    usuario = consultar_usuario(reserva["userId"])

    # Crear la factura
    factura = Invoice(
        reserva_id=reserva_id,
        monto_total=reserva["totalAmount"],
        fecha=datetime.utcnow()
    )
    
    collection = get_mongo_client()
    factura_id = collection.insert_one(factura.to_dict()).inserted_id

    return {
        "factura_id": str(factura_id),
        "reserva": reserva,
        "usuario": usuario,
        "monto_total": reserva["totalAmount"],
        "fecha": factura.fecha
    }
