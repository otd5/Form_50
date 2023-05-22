import qrcode
import sqlite3
import csv
import loguru


def make_qrcode():

    conn = sqlite3.connect('database/medical_db.db')
    c = conn.cursor()
    c.execute("""SELECT name, number_token_fighter, number_part,
              date, identified_injuries, medical_care_provided,
              sanitary_treatment, diagnosis, priority,
              medic_data FROM wounded_fighter""")
    records = c.fetchall()
    loguru.logger.info("Данные из базы получены")

    with open('static_fiels/data_of_wounded.csv', "w") as the_file:
        csv.register_dialect("custom", delimiter=",",
                             skipinitialspace=True)
        writer = csv.writer(the_file, dialect="custom")
        writer.writerow(records[0])
        writer.writerow(records[1])
        writer.writerow(records[2])
        writer.writerow(records[3])

    with open("static_fiels/data_of_wounded.csv") as f:
        date = f.read()
        code = qrcode.QRCode(version=1.0, box_size=15, border=4)
        code.add_data(date)
        code.make(fit=True)
        img = code.make_image(fill='Black', back_color='White')
        # сохраняем img в файл
        img.save("static_fiels/site.png")
        loguru.logger.info("Qr code сформирован")
