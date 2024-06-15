import sqlite3


class Card:

    database = "banking.db"

    def __init__(self, card_circuit: str, card_number: str, card_cvc: str, card_holder: str):
        self.card_circuit = card_circuit
        self.card_number = card_number
        self.card_cvc = card_cvc
        self.card_holder = card_holder

    def is_valid(self, seat_price):

        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "type", "number", "cvc", "holder", "balance" FROM "Card" WHERE number=?
        """, [self.card_number])
        card_data: list[list[tuple]] = cursor.fetchall()
        connection.close()

        if self.card_circuit == card_data[0][0] and self.card_number == card_data[0][1] \
            and self.card_cvc == card_data[0][2] and self.card_holder == card_data[0][3] \
                and card_data[0][4] >= seat_price:
            return True
        else:
            return False
