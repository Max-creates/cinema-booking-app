from card import Card
from pdfbuilder import PdfBuilder
from qrcodegenerator import QRCodeGenerator
from seat import Seat
from user import User
from ticket import Ticket
import sqlite3


def load_all_seats():
    database = "cinema.db"
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT * FROM Seat
    """)
    data = cursor.fetchall()
    connection.close()
    return data


def print_all_seats_data(all_seats_data):
    for seat in all_seats_data:
        print(f"Seat number: {seat[0]} - {'Occupied' if seat[1] != 0 else 'Free'} - price: {seat[2]}")


while True:
    all_seats = load_all_seats()
    full_name = input("Your full name: ")

    print_all_seats_data(all_seats)

    selected_seat = input("Preferred seat number: ")
    if Seat(selected_seat).is_free():
        seat = Seat(selected_seat)
        print(f"Selected: {selected_seat} Price: {seat.price}")
    else:
        print("Seat occupied...")
        continue

    user = User(full_name)
    card_type: str = input("Your card type: ")
    card_number: str = input("Your card number: ")
    card_cvc: str = input("Your card cvc: ")
    card_holder: str = input("Card holder name: ")
    card = Card(card_type, card_number, card_cvc, card_holder)
    if card.is_valid(seat.price):
        user.buy(seat, card_number)
        seat.occupy()
        ticket = Ticket(user.name, seat.price, seat.seat_id)
        qrcode = QRCodeGenerator(ticket)
        qr_image = qrcode.generate()
        qrcode.save_to_png(qr_image)
        pdf = PdfBuilder(ticket)
        pdf.generate(f'{ticket.seat}_qr.png')
        print("Purchase Successful!")
    else:
        print("There was a problem with your card.")


