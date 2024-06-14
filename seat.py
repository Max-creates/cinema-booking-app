import sqlite3


class Seat:
    def __init__(self, number: str):
        self.seat_id = number

        connection = sqlite3.connect("cinema.db")
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT "price" FROM "Seat" WHERE seat_id=?
        """, [self.seat_id])
        price: list[list[tuple]] = cursor.fetchall()
        connection.close()
        self.price = price[0][0]

    def is_free(self):
        connection = sqlite3.connect("cinema.db")
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT "taken" FROM "Seat" WHERE seat_id=?
        """, [self.seat_id])
        result: list[list[tuple]] = cursor.fetchall()
        connection.close()
        if result[0][0] == 0:
            return True
        else:
            return False

    def occupy(self):
        connection = sqlite3.connect("cinema.db")
        connection.execute(f"""
        UPDATE "Seat" SET "taken"=1 WHERE seat_id=?
        """, [self.seat_id])
        connection.commit()
        connection.close()
