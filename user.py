import sqlite3


class User:
    def __init__(self, name: str):
        self.name = name

    def buy(self, seat, card):
        seat.occupy()

        connection = sqlite3.connect("banking.db")
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE number=?
        """, [card])
        balance: list = cursor.fetchall()
        connection.close()
        balance: float = float(balance[0][0])
        update_balance: str = balance - seat.price

        connection = sqlite3.connect("banking.db")
        connection.execute("""
        UPDATE "Card" SET "balance"=? WHERE number=?
        """, [update_balance, card])
        connection.commit()
        connection.close()
