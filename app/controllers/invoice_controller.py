from flask import Blueprint, jsonify, request
from app.services.soap_service import generate_invoice

invoice_bp = Blueprint("invoice", __name__, url_prefix="/invoice")

@invoice_bp.route("/generate_invoice", methods=["POST"])
def generate_invoice_endpoint():
    """Endpoint to generate an invoice."""
    data = request.get_json()
    reservation_id = data.get("reservation_id")
    if not reservation_id:
        return jsonify({"error": "Reservation ID is required"}), 400

    try:
        response = generate_invoice(reservation_id)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
