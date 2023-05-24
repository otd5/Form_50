from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def evacuation_method_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Автомобиль",
            "on_release":
                lambda x="Автомобиль": self.set_evacuation_method_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Бронемашина",
            "on_release": lambda x="Бронемашина":
                self.set_evacuation_method_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Спецборт",
            "on_release":
                lambda x="Спецборт":
                    self.set_evacuation_method_item(x),
        }
        ]

    self.menu = MDDropdownMenu(
        caller=self.ids.evacuation_method,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
