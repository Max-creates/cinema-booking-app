import random
import string


class Ticket:
    def __init__(self, user: str, price, seat: str):
        generate_id = ''.join(random.choices(string.ascii_letters, k=10))
        self.ticket_id = generate_id
        self.user = user
        self.price = price
        self.seat = seat
