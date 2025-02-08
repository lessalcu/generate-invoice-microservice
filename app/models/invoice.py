class Invoice:
    def __init__(self, reservation_id, total_amount, date):
        self.reservation_id = reservation_id
        self.total_amount = total_amount
        self.date = date

    def to_dict(self):
        return {
            "reservation_id": self.reservation_id,
            "total_amount": self.total_amount,
            "date": self.date
        }
