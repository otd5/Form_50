from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from datetime import datetime


def medical_care_provided_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Антибиотик",
            "on_release":
                lambda x="Антибиотик": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Сыворотка ПСС, ПГС",
            "on_release":
                lambda x="Сыворотка ПСС, ПГС": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Анатоксин (какой)",
            "on_release":
                lambda x="Анатоксин (какой)": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Антидот (какой)",
            "on_release":
                lambda x="Антидот (какой)": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Обезболивающее средство",
            "on_release": (
                lambda x="Обезболивающее средство":
                    self.set_item_medical(x)),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Переливание крови",
            "on_release":
                lambda x="Переливание крови": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Переливание кровезаменителей",
            "on_release":
                (lambda x="Переливание кровезаменителей":
                    self.set_item_medical(x)),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Иммобилизация",
            "on_release":
                lambda x="Иммобилизация": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Перевязывание",
            "on_release":
                lambda x="Перевязывание": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Жгут, дата и время наложения",
            "on_release": (
                lambda x=f"""Жгут {datetime.now().strftime
                ('%Y-%m-%d %H:%M:%S')}""":
                    self.set_item_medical(x))
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Нет",
            "on_release": (
                lambda x="Медецинской помощи не потребовалось":
                    self.set_item_medical(x)),
        }
    ]

    self.menu = MDDropdownMenu(
        caller=self.ids.medical,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
