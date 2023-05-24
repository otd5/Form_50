from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def evacuation_queue_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Первоочередной",
            "on_release":
                lambda x="1": self.set_evacuation_queue_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Второстепенный",
            "on_release": lambda x="2":
                self.set_evacuation_queue_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Не требует срочной помощи",
            "on_release":
                lambda x="3":
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
