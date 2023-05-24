from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def evacuation_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Сидя",
            "on_release":
                lambda x="Сидя": self.set_evacuation_medical(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Лежа",
            "on_release": lambda x="Лежа": self.set_evacuation_medical(x),
        }, ]

    self.menu = MDDropdownMenu(
        caller=self.ids.where_delivered,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
