import qrcode
import sqlite3
import csv
import loguru


def make_qrcode():

    conn = sqlite3.connect('database/medical_person.db')
    c = conn.cursor()
    c.execute("""SELECT number_docs, surname, age,
                floor, affiliation, rank, military_unit, reason,
                diagnosis, voluntary_consent, first_aid, medical,
                evacuation,
                evacuation_queue, evacuation_method, where_delivered,
                name_doctor, datetime FROM medical_db""")
    records = c.fetchall()
    loguru.logger.info("Данные из базы получены")

    with open('static_fiels/data_of_wounded.csv', "w") as the_file:
        csv.register_dialect("custom", delimiter=",",
                             skipinitialspace=True)
        writer = csv.writer(the_file, dialect="custom")
        writer.writerow(records[0])
        writer.writerow(records[1])

    with open("static_fiels/data_of_wounded.csv") as f:
        date = f.read()
        code = qrcode.QRCode(version=1.0, box_size=15, border=4)
        code.add_data(date)
        code.make(fit=True)
        img = code.make_image(fill='Black', back_color='White')
        # сохраняем img в файл
        img.save("static_fiels/site.png")
        loguru.logger.info("Qr code сформирован")
