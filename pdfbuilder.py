from fpdf import FPDF
from qrcodegenerator import QRCodeGenerator
import os
from ticket import Ticket


class PdfBuilder(FPDF):
    """Class to build a PDF document using ticket data. To initialize provide ticket object as argument."""
    def __init__(self, ticket: Ticket):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.ticket = ticket

    def generate(self, qr_image: str, save_qr_image_flag: bool = False):
        """Generate pdf page with ticket data and qr image,
        argument must be a string path to the image for example: 'qr_image.png' or
        'images/qr_image.png'.
        Optional argument bool:
        False - to delete the qr image after pdf is generated,
        True - to save the qr image after pdf is generated.
        """
        self.add_page()

        self.set_font("Arial", "B", 30)

        self.cell(w=0, h=30, txt="Your Digital Ticket", border=1, align="C", ln=1)

        self.set_font("Arial", "B", 15)
        self.cell(w=40, h=10, txt="Name", border=1)
        self.set_font("Arial", "", 13)
        self.cell(w=100, h=10, txt=self.ticket.user, border=1, ln=1)
        self.image(qr_image, w=40, h=40, x=155, y=41)

        self.set_font("Arial", "B", 15)
        self.cell(w=40, h=10, txt="Ticket ID", border=1)
        self.set_font("Arial", "", 13)
        self.cell(w=100, h=10, txt=self.ticket.ticket_id, border=1, ln=1)

        self.set_font("Arial", "B", 15)
        self.cell(w=40, h=10, txt="Price", border=1)
        self.set_font("Arial", "", 13)
        self.cell(w=100, h=10, txt=f"{self.ticket.price}", border=1, ln=1)

        self.set_font("Arial", "B", 15)
        self.cell(w=40, h=10, txt="Seat Number", border=1)
        self.set_font("Arial", "", 13)
        self.cell(w=100, h=10, txt=self.ticket.seat, border=1, ln=1)

        self.output(f"{self.ticket.seat}_ticket.pdf")

        if not save_qr_image_flag:
            os.remove(f'{self.ticket.seat}_qr.png')


if __name__ == '__main__':
    ticket = Ticket('Johny Smith', 50, '98')
    qrcode = QRCodeGenerator(ticket)
    qr_image = qrcode.generate()
    qrcode.save_to_png(qr_image)
    pdf = PdfBuilder(ticket)
    pdf.generate(f'{ticket.seat}_qr.png')