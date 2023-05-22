import sqlite3
import loguru


def on_click(self):  # Метод действие кнопки
    conn = sqlite3.connect('database/medical_db.db')
    c = conn.cursor()
    c.execute("""INSERT INTO wounded_fighter VALUES (:id ,:name, :token,
                :num_part, :date, :menu, :medical, :sanitary,
                :diagnosis, :priority, :date_med)""", {
                'id': None,
                'name': self.surname.text,
                'token': self.num_token.text,
                'num_part': self.num_part.text,
                'date': None,
                'menu': self.ids.menu.text,
                'medical': self.ids.medical.text,
                'sanitary': self.ids.sanitary.text,
                'diagnosis': self.ids.diagnosis.text,
                'priority': self.ids.priority.text,
                'date_med': self.ids.name_doctor.text
                })
    conn.commit()
    loguru.logger.info("Данные добавлены")
    conn.close()
