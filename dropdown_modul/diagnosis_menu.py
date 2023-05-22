from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from datetime import datetime


def diagnosis_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Ранение",
            "on_release":
                lambda x="Ранение (Указать часть тела)":
                    self.set_diagnosis_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Ожог",
            "on_release":
                lambda x="Ожог (Указать % и часть тела)":
                    self.set_diagnosis_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Отрыв конечности(Какой)",
            "on_release":
                lambda x="Отрыв конечности (какой)":
                    self.set_diagnosis_item(x),
        },

        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Перевязывание",
            "on_release":
                lambda x="Перевязывание": self.set_diagnosis_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Жгут, дата и время наложения",
            "on_release": (
                lambda x=f"""Жгут {datetime.now().strftime
                ('%Y-%m-%d %H:%M:%S')}""":
                    self.set_diagnosis_item(x))
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Нет",
            "on_release": (
                lambda x="Медецинской помощи не потребовалось":
                    self.set_diagnosis_item(x)),
        }
    ]

    self.menu = MDDropdownMenu(
        caller=self.ids.diagnosis,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
