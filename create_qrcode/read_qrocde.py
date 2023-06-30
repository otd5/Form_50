from kivymd.uix.snackbar import Snackbar
import csv
import loguru
from .dropdown_decode import decode_qrcode


def on_symbols_(self, instance, symbols):

    if not symbols == "":
        for symbol in symbols:
            loguru.logger.info("Qr code расшифрован")
            self.decode_text = symbol.data.decode()
            Snackbar(
                    text="QR-code расшифрован",
                    snackbar_x="10dp",
                    snackbar_y="10dp",
                    size_hint_x=.7,
                    md_bg_color="green",
                    font_size=25

            ).open()
        self.decode_date = decode_qrcode(self.decode_text)

        with open('static_fiels/data_of_qrcode.csv', "w", newline='',
                  encoding='UTF-8') as the_file:
            csv.register_dialect("custom", delimiter=",",
                                 skipinitialspace=True,
                                 )
            writer = csv.writer(the_file, dialect="custom")
            for row in self.decode_date:
                writer.writerow(row)

    else:
        loguru.logger.error("Qr code не получен")
