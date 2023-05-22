from kivymd.uix.snackbar import Snackbar
import csv
import loguru


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
        self.decode_date = self.decode_text.strip().split(',')

        with open('static_fiels/data_of_qrcode.csv', "w") as the_file:
            csv.register_dialect("custom", delimiter=",",
                                 skipinitialspace=True,
                                 lineterminator='"')
            writer = csv.writer(the_file, dialect="custom")
            writer.writerow(self.decode_date)
    else:
        loguru.logger.error("Qr code не получен")
