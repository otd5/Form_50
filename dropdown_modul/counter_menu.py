from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
# import csv
import sqlite3


def counter_mod(self):
    conn = sqlite3.connect('database/medical_person.db')
    c = conn.cursor()
    # c.execute("""SELECT number_docs FROM medical_db DESC LIMIT 1""")
    c.execute("""SELECT number_docs FROM
              medical_db ORDER BY rowid DESC LIMIT 1""")
    records = c.fetchall()
    number_docs_counter = ''
    for item in records:
        number_docs_counter = item

    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": f"{number_docs_counter[0] + 1}",
            "on_release":
                lambda x=f"{number_docs_counter[0] + 1}":
                    self.set_document_number_item(x),
        },
        ]

    self.menu = MDDropdownMenu(
        caller=self.ids.document_number,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
