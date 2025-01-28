import sqlite3


class Seat:

    database = "cinema.db"

    def __init__(self, seat_id: str):
        self.seat_id = seat_id
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT "price" FROM "Seat" WHERE seat_id=?
        """, [self.seat_id])
        price: list[list[tuple]] = cursor.fetchall()[0][0]
        connection.close()
        self.price = price


    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT "taken" FROM "Seat" WHERE seat_id=?
        """, [self.seat_id])
        result: list[list[tuple]] = cursor.fetchall()[0][0]
        connection.close()
        return result == 0:


    def occupy(self):
        connection = sqlite3.connect(self.database)
        connection.execute(f"""
        UPDATE "Seat" SET "taken"=1 WHERE seat_id=?
        """, [self.seat_id])
        connection.commit()
        connection.close()
