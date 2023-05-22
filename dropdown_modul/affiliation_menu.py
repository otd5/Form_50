from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def affiliation_menu_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Вооруженные силы",
            "on_release":
                lambda x="Вооруженные силы": self.set_affiliation_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Гражданский персонал",
            "on_release": lambda x="Гражданский персонал":
                    self.set_affiliation_item(x),
        }, ]

    self.menu = MDDropdownMenu(
        caller=self.ids.affiliation,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
