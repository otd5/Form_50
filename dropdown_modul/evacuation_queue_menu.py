from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def evacuation_queue_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "I",
            "on_release":
                lambda x="Первая": self.set_evacuation_queue_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "II",
            "on_release": lambda x="Вторая":
                self.set_evacuation_queue_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "III",
            "on_release":
                lambda x="Третья":
                    self.set_evacuation_queue_item(x),
        }
        ]

    self.menu = MDDropdownMenu(
        caller=self.ids.first_aid,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
