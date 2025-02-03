from services.invoice_service import generar_factura

def procesar_factura(reserva_id):
    """Punto de entrada para generar una factura."""
    return generar_factura(reserva_id)
