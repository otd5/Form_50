import sqlite3
import csv
from loguru import logger
from kivymd.uix.snackbar import Snackbar

logger.add('logging/logging.log',
           format='''{time} {name} {function} {line} {level} {message}''',
           level="DEBUG", rotation="10KB", compression="zip")


def qrcode_to_db_(self):

    conn = sqlite3.connect('database/medical_db.db')
    c = conn.cursor()
    try:
        if self.decode_date is not None:
            file = open('static_fiels/data_of_qrcode.csv')
            contents = csv.reader(file)
            insert_records = """INSERT INTO wounded_fighter(name,
                number_token_fighter, number_part,
                date, identified_injuries, medical_care_provided,
                                sanitary_treatment, diagnosis,
                                priority, medic_data)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            c.executemany(insert_records, contents)
            conn.commit()
            conn.close()
    except AttributeError:
        logger.error("Отправлено пустое значение")
        Snackbar(
            text="Пустое значение",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.7,
            md_bg_color="green",
            font_size=25

            ).open()

    # conn = sqlite3.connect('static_fiels/medical_db.db')
    # c = conn.cursor()
    # try:
    #     if self.decode_date is not None:
    #         print(self.decode_date)
    #         c.execute("""INSERT INTO wounded_fighter VALUES (
    #                     :id ,:name, :token,
    #                     :num_part, :date, :menu, :medical, :sanitary,
    #                     :diagnosis, :priority, :date_med)""", {
    #                     'id': None,
    #                     'name': self.decode_date[0],
    #                     'token': self.decode_date[1],
    #                     'num_part': self.decode_date[2],
    #                     'date': self.decode_date[3],
    #                     'menu': self.decode_date[4],
    #                     'medical': self.decode_date[5],
    #                     'sanitary': self.decode_date[6],
    #                     'diagnosis': self.decode_date[7],
    #                     'priority': self.decode_date[8],
    #                     'date_med': self.decode_date[9],
    #                     })
    #         conn.commit()
    #         conn.close()
    # except AttributeError:
    #     logger.error("Отправлено пустое значение")
    #     Snackbar(
    #         text="Пустое значение",
    #         snackbar_x="10dp",
    #         snackbar_y="10dp",
    #         size_hint_x=.7,
    #         md_bg_color="green",
    #         font_size=25

    #         ).open()
