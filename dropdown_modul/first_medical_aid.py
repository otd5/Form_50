from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def first_medical_aid_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Оказана",
            "on_release":
                lambda x="Оказана": self.set_first_medical_aid_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Не оказана",
            "on_release": lambda x="Не оказана":
                self.set_first_medical_aid_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Не требовалась",
            "on_release":
                lambda x="Не требовалась":
                    self.set_first_medical_aid_item(x),
        }
        ]

    self.menu = MDDropdownMenu(
        caller=self.ids.first_aid,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
