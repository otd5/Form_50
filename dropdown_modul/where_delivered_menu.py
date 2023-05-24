from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def where_delivered_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Мед. пункт",
            "on_release":
                lambda x="Мед. пункт": self.set_where_delivered_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "МОСН",
            "on_release": lambda x="МОСН":
                self.set_where_delivered_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Госпиталь",
            "on_release":
                lambda x="Госпиталь":
                    self.set_where_delivered_item(x),
        }
        ]

    self.menu = MDDropdownMenu(
        caller=self.ids.voluntary_consent,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
