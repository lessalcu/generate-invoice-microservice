class Invoice:
    def __init__(self, reserva_id, monto_total, fecha):
        self.reserva_id = reserva_id
        self.monto_total = monto_total
        self.fecha = fecha

    def to_dict(self):
        return {
            "reserva_id": self.reserva_id,
            "monto_total": self.monto_total,
            "fecha": self.fecha
        }
