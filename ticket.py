import random
import string
from fpdf import FPDF
from qrcode import QRCode


class Ticket:
    def __init__(self, user: str, price, seat: str):
        generate_id = ''.join(random.choices(string.ascii_letters, k=10))
        self.ticket_id = generate_id
        self.user = user
        self.price = price
        self.seat = seat
        self.generate_qr()


    def to_pdf(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font("Arial", "B", 30)

        pdf.cell(w=0, h=30, txt="Your Digital Ticket", border=1, align="C", ln=1)

        pdf.set_font("Arial", "B", 15)
        pdf.cell(w=40, h=10, txt="Name", border=1)
        pdf.set_font("Arial", "", 13)
        pdf.cell(w=100, h=10, txt=self.user, border=1, ln=1)
        pdf.image(f'{self.seat}_qr.png', w=40, h=40, x=155, y=41)

        pdf.set_font("Arial", "B", 15)
        pdf.cell(w=40, h=10, txt="Ticket ID", border=1)
        pdf.set_font("Arial", "", 13)
        pdf.cell(w=100, h=10, txt=self.ticket_id, border=1, ln=1)

        pdf.set_font("Arial", "B", 15)
        pdf.cell(w=40, h=10, txt="Price", border=1)
        pdf.set_font("Arial", "", 13)
        pdf.cell(w=100, h=10, txt=f"{self.price}", border=1, ln=1)

        pdf.set_font("Arial", "B", 15)
        pdf.cell(w=40, h=10, txt="Seat Number", border=1)
        pdf.set_font("Arial", "", 13)
        pdf.cell(w=100, h=10, txt=self.seat, border=1, ln=1)

        pdf.output(f"{self.seat}_ticket.pdf")

    def generate_qr(self):
        qr_code = QRCode(box_size=10, border=1)
        qr_code.add_data(f'Ticket ID: {self.ticket_id}, Name: {self.user}, '
                         f'Seat: {self.seat}, Price: {self.price}')
        qr_image = qr_code.make_image(fill_color='black', back_color='white')
        qr_image.save(f'{self.seat}_qr.png')


if __name__ == '__main__':
    ticket = Ticket('John Smith', 50, 'A99')
    ticket.to_pdf()
