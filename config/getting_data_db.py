import sqlite3
import loguru


def view_all_name(self):

    conn = sqlite3.connect('database/medical_person.db')
    c = conn.cursor()
    c.execute("""SELECT surname, evacuation_queue FROM medical_db""")
    records = c.fetchall()
    if not records:
        loguru.logger.error("База данных пуста")
        self.ids.labled.text = "Данные отсутствуют"
    else:
        one = ''
        two = ''
        three = ''
        for item in records:
            if item[1] == 'Первая':
                one += f'{item[0]}\n'
            elif item[1] == 'Вторая':
                two += f'{item[0]}\n'
            elif item[1] == 'Третья':
                three += f'{item[0]}\n'
        self.ids.labled.text = f"""[Тяжело раненные]\n{one}
                                    \n [Средней тяжести]\n {two}
                                    \n [Легкие ранения]\n{three}"""
        conn.commit()
        conn.close()
