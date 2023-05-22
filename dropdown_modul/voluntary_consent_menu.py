from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def voluntary_consent_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Согласен",
            "on_release":
                lambda x="Согласен": self.set_voluntary_consent_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Не согласен",
            "on_release": lambda x="Не согласен":
                self.set_voluntary_consent_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Бессознательное состояние",
            "on_release":
                lambda x="Бессознательное состояние":
                    self.set_voluntary_consent_item(x),
        }
        ]

    self.menu = MDDropdownMenu(
        caller=self.ids.voluntary_consent,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
