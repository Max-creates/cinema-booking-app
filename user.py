import sqlite3


class User:

    database = "banking.db"

    def __init__(self, name: str):
        self.name = name

    def buy(self, seat, card):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT "balance" FROM "Card" WHERE number=?
            """, [card])
            balance = cursor.fetchone()[0]
            update_balance = balance - seat.price
            connection.execute("""
            UPDATE "Card" SET "balance"=? WHERE number=?
            """, [update_balance, card])
            connection.commit()
