import sqlite3


class Card:

    database = "banking.db"

    def __init__(self, card_circuit: str, card_number: str, card_cvc: str, card_holder: str):
        self.card_circuit = card_circuit
        self.card_number = card_number
        self.card_cvc = card_cvc
        self.card_holder = card_holder

    def is_valid(self, seat_price):

        # Using context manager to ensure the connection is properly closed.
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT "type", "number", "cvc", "holder", "balance" FROM "Card" WHERE number=?
            """, [self.card_number])
            card_data = cursor.fetchone()

        # This is a good check for empty results to prevent runtime errors.
        if not card_data:
            return False  # Card does not exist

        card_type, number, cvc, holder, balance = card_data

        return (
            self.card_circuit == card_type and
            self.card_number == number and
            self.card_cvc == cvc and
            self.card_holder == holder and
            balance >= seat_price
        )

