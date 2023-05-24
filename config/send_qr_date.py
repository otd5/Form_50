import sqlite3
import csv
from loguru import logger
from kivymd.uix.snackbar import Snackbar

logger.add('logging/logging.log',
           format='''{time} {name} {function} {line} {level} {message}''',
           level="DEBUG", rotation="10KB", compression="zip")


# TODO Исправить столбцы из запроса в бд
def qrcode_to_db_(self):

    conn = sqlite3.connect('database/medical_person.db')
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

