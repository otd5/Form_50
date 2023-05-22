import sqlite3
import loguru


def view_all_name(self):

    conn = sqlite3.connect('database/medical_db.db')
    c = conn.cursor()
    c.execute("""SELECT name, priority FROM wounded_fighter""")
    records = c.fetchall()
    if not records:
        loguru.logger.error("База данных пуста")
        self.ids.labled.text = "Данные отсутствуют"
    else:
        one = ''
        two = ''
        three = ''
        for item in records:
            if item[1] == 1:
                one += f'{item[0]}\n'
            elif item[1] == 2:
                two += f'{item[0]}\n'
            elif item[1] == 3:
                three += f'{item[0]}\n'
        self.ids.labled.text = f"""[Тяжело раненные]\n{one}
                                    \n [Средней тяжести]\n {two}
                                    \n [Легкие ранения]\n{three}"""
        conn.commit()
        conn.close()
