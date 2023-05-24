from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from datetime import datetime


def medical_care_provided_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Повязка на руку",
            "on_release":
                lambda x="Повязка на руку": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Давящая повязка",
            "on_release":
                lambda x="Давящая повязка": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Тампонада раны",
            "on_release":
                lambda x="Тампонада раны": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Зажим (лигатура) на сосуд",
            "on_release":
                lambda x="Зажим (лигатура) на сосуд": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Жгут, дата и время наложения",
            "on_release": (
                lambda x=f"""Жгут {datetime.now().strftime
                ('%Y-%m-%d %H:%M:%S')}""":
                    self.set_item_medical(x)),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Контроль жгута",
            "on_release":
                lambda x="Контроль жгута": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Очищение ротоглотки",
            "on_release":
                (lambda x="Очищение ротоглотки":
                    self.set_item_medical(x)),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Воздуховод",
            "on_release":
                lambda x="Воздуховод": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Прошивание языка",
            "on_release":
                lambda x="Прошивание языка": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "ИВЛ",
            "on_release":
                lambda x="ИВЛ": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Ингаляция кислорода",
            "on_release": (
                lambda x="Ингаляция кислорода":
                    self.set_item_medical(x)),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Аспирация из трахеи",
            "on_release":
                lambda x="Аспирация из трахеи": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Конкотез иглами",
            "on_release":
                lambda x="Конкотез иглами": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Конкокритомия",
            "on_release":
                lambda x="Конкокритомия": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Трахеостомия",
            "on_release":
                lambda x="Трахеостомия": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Окклюзионная повязка",
            "on_release":
                lambda x="Окклюзионная повязка": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Выведение мочи",
            "on_release":
                lambda x="Выведение мочи": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Антибиотк",
            "on_release":
                (lambda x="Антибиотик":
                    self.set_item_medical(x)),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Антитаксин",
            "on_release":
                lambda x="Антитаксин": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Сыворотка",
            "on_release":
                lambda x="Сыворотка": self.set_item_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Антидот",
            "on_release":
                lambda x="Антидот": self.set_item_medical(x),
        }
    ]

    self.menu = MDDropdownMenu(
        caller=self.ids.medical,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
