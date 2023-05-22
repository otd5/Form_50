from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def floor_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Мужской",
            "on_release":
                lambda x="Мужской": self.set_floor_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Женский",
            "on_release": lambda x="Женский": self.set_floor_item(x),
        }, ]

    self.menu = MDDropdownMenu(
        caller=self.ids.floor,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
