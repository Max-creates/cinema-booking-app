from card import Card
from seat import Seat
from user import User
from ticket import Ticket

while True:
    full_name: str = input("Your full name: ")
    user1 = User(full_name)
    selected_seat: str = input("Preferred seat number: ")
    if Seat(selected_seat).is_free():
        user1_seat = Seat(selected_seat)
        print(f"{selected_seat} is free. Price: {user1_seat.price}")
    else:
        print("Seat occupied...")
        continue

    card_type: str = input("Your card type: ")
    card_number: str = input("Your card number: ")
    card_cvc: str = input("Your card cvc: ")
    holder_name: str = input("Card holder name: ")
    card = Card(card_type, card_number, card_cvc, holder_name)
    if card.is_valid(user1_seat.price):
        user1.buy(user1_seat, card_number)
        ticket = Ticket(user1.name, user1_seat.price, user1_seat.seat_id)
        ticket.to_pdf()
        print("Purchase Successful!")
    else:
        print("There was a problem with your card.")


