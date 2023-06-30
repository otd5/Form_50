from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def military_rank_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Рядовой",
            "on_release":
                lambda x="Рядовой": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Ефрейтор",
            "on_release": lambda x="Ефрейтор": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Младший сержант",
            "on_release": lambda x="Младший сержант": 
                self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Сержант",
            "on_release": lambda x="Сержант": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Старший сержант",
            "on_release":
                lambda x="Старший сержант": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Старшина",
            "on_release": lambda x="Старшина": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Прапорщик",
            "on_release": lambda x="Прапорщик": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Старший прапорщик",
            "on_release": lambda x="Старший прапорщик":
                self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Лейтенант",
            "on_release": lambda x="Лейтенант": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Старший лейтенант",
            "on_release": lambda x="Старший лейтенант":
                self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Капитан",
            "on_release": lambda x="Капитан": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Майор",
            "on_release": lambda x="Майор": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Подполковник",
            "on_release":
                lambda x="Подполковник": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Полковник",
            "on_release": lambda x="Полковник": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Генерал майор",
            "on_release": lambda x="Генерал майор": self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Генерал лейтенант",
            "on_release": lambda x="Генерал лейтенант": 
                self.set_military_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Генерал полковник",
            "on_release": lambda x="Генерал полковник":
                self.set_military_item(x),
        }
    ]

    self.menu = MDDropdownMenu(
        caller=self.ids.rank,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
