import sqlite3


class User:

    database = "banking.db"

    def __init__(self, name: str):
        self.name = name

    def buy(self, seat, card):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Card" WHERE number=?
        """, [card])
        balance = cursor.fetchall()[0][0]
        update_balance = balance - seat.price
        connection.execute("""
        UPDATE "Card" SET "balance"=? WHERE number=?
        """, [update_balance, card])
        connection.commit()
        connection.close()
