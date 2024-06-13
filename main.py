import sqlite3
import random
import string


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
        self.price: tuple[float] = price[0][0]

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


class Card:
    def __init__(self, card_circuit: str, card_number: str, card_cvc: str, card_holder: str):
        self.card_circuit = card_circuit
        self.card_number = card_number
        self.card_cvc = card_cvc
        self.card_holder = card_holder

    def is_valid(self, seat_price):

        connection = sqlite3.connect("banking.db")
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


class Ticket:
    def __init__(self, user, price, seat):
        generate_id = ''.join(random.choices(string.ascii_letters, k=6))
        self.ticket_id = generate_id
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self):
        pass


while True:
    full_name: str = input("Your full name: ")
    user1 = User(full_name)
    selected_seat: str = input("Preferred seat number: ")
    if Seat(selected_seat).is_free():
        user1_seat = Seat(selected_seat)
        print(f"{selected_seat} is free.")
    else:
        print("Seat occupied...")
        continue

    card_type: str = input("Your card type: ")
    card_number: str = input("Your card number: ")
    card_cvc: str = input("Your card cvc: ")
    holder_name: str = input("Card holder name: ")
    card = Card(card_type, card_number, card_cvc, holder_name)
    if card.is_valid(user1_seat.price):
        print("Your card is valid.")
        user1.buy(user1_seat, card_number)
    else:
        print("There was a problem with your card.")


