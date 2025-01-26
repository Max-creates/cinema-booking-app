from qrcode import QRCode
from ticket import Ticket


class QRCodeGenerator(QRCode):
    """Class to generate qr code using ticket data. To initialize provide ticket object as argument."""
    def __init__(self, ticket: Ticket):
        super().__init__(box_size=10, border=1)
        self.ticket: Ticket = ticket

    def generate(self) -> "QRCode.Image":
        self.add_data(f'Ticket ID: {self.ticket.ticket_id}, Name: {self.ticket.user}, '
                      f'Seat: {self.ticket.seat}, Price: {self.ticket.price}')
        return self.make_image(fill_color='black', back_color='white')

    def save_to_png(self, qr_image: "QRCode.Image") -> None:
        qr_image.save(f'{self.ticket.seat}_qr.png')
