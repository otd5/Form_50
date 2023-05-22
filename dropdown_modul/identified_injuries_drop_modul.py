from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def identified_injuries_drop_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Огнестрельное оружие",
            "on_release":
                lambda x="Огнестрельное оружие": self.set_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Ядерное оружие",
            "on_release": lambda x="Ядерное оружие": self.set_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Химическое оружие",
            "on_release": lambda x="Химическое оружие": self.set_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Обморожение",
            "on_release": lambda x="Обморожение": self.set_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Бактериологическое оружие",
            "on_release":
                lambda x="Бактериологические оружие": self.set_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Больной",
            "on_release": lambda x="Больной": self.set_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Особо Опастные инфекции",
            "on_release": lambda x="Особо опасные инфекции": self.set_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Другие ранения",
            "on_release": lambda x="Другие ранения": self.set_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Нет",
            "on_release": lambda x="Ранения отсутствуют": self.set_item(x),
        }
    ]

    self.menu = MDDropdownMenu(
        caller=self.ids.menu,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
