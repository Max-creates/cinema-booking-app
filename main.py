from card import Card
from seat import Seat
from user import User
from ticket import Ticket

while True:
    full_name: str = input("Your full name: ")
    selected_seat: str = input("Preferred seat number: ")
    if Seat(selected_seat).is_free():
        seat = Seat(selected_seat)
        print(f"{selected_seat} is free. Price: {seat.price}")
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
        ticket = Ticket(user.name, seat.price, seat.seat_id)
        ticket.to_pdf()
        print("Purchase Successful!")
    else:
        print("There was a problem with your card.")


