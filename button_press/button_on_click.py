import sqlite3
import loguru


def on_click(self):  # Метод действие кнопки
    conn = sqlite3.connect('database/medical_person.db')
    c = conn.cursor()
    c.execute("""INSERT INTO medical_db VALUES (:id , :surname, :age,
                :floor, :affiliation, :rank, :military_unit, :reason,
                :diagnosis, :voluntary_consent, :first_aid, :medical,
                :evacuation,
                :evacuation_queue, :evacuation_method, :where_delivered,
                :name_doctor, :date)""", {
                'id': None,
                'surname': self.ids.surname.text,
                'age': self.ids.age.text,
                'floor': self.ids.floor.text,
                'affiliation': self.ids.affiliation.text,
                'rank': self.ids.rank.text,
                'military_unit': self.ids.military_unit.text,
                'reason': self.ids.reason.text,
                'diagnosis': self.ids.diagnosis.text,
                'voluntary_consent': self.ids.voluntary_consent.text,
                'first_aid': self.ids.first_aid.text,
                'medical': self.ids.medical.text,
                'evacuation': self.ids.evacuation.text,
                'evacuation_queue': self.ids.evacuation_queue.text,
                'evacuation_method': self.ids.evacuation_method.text,
                'where_delivered': self.ids.where_delivered.text,
                'name_doctor': self.ids.name_doctor.text,
                'date': None,

                })
    conn.commit()
    loguru.logger.info("Данные добавлены")
    conn.close()
