from flask import Blueprint, jsonify, request
from app.services.soap_service import generar_factura

invoice_bp = Blueprint("invoice", __name__)

@invoice_bp.route("/soap/generar_factura", methods=["POST"])
def generar_factura_endpoint():
    """Endpoint para generar una factura."""
    data = request.get_json()
    reserva_id = data.get("reserva_id")
    if not reserva_id:
        return jsonify({"error": "Debe proporcionar el ID de la reserva"}), 400

    try:
        response = generar_factura(reserva_id)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
