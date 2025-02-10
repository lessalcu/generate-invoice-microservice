from app.services.invoice_service import generate_invoice

def process_invoice(reservation_id):
    """Entry point to generate an invoice."""
    return generate_invoice(reservation_id)
