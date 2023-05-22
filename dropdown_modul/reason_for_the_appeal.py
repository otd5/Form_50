from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


def reason_for_the_appeal_mod(self):
    self.menu_list = [
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Заболевание",
            "on_release":
                lambda x="Заболевание": self.set_reason_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Бытовая травма",
            "on_release":
                lambda x="Бытовая травма": self.set_reason_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Механическая травма",
            "on_release":
                lambda x="Механическая травма": self.set_reason_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Производственная травма",
            "on_release":
                lambda x="Производственная травма": self.set_reason_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Огнестрельное ранение",
            "on_release":
                lambda x="Огнестрельное ранение":
                    self.set_reason_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Осколочное ранение",
            "on_release":
                lambda x="Осколочное ранение": self.set_reason_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Минно-взрывная травма",
            "on_release":
                lambda x="Минно-взрывная травма":
                    self.set_reason_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Резаные и колотые раны",
            "on_release":
                lambda x="Резаные и колотые раны": self.set_reason_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Колотые проникающие раны",
            "on_release":
                lambda x="Колотые проникающие раны": self.set_reason_item(x),
        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Ожог",
            "on_release":
                lambda x="Ожог": self.set_reason_item(x),

        },
        {
            "viewclass": "OneLineListItem",
            "height": dp(56),
            "text": "Рваные раны",
            "on_release":
                lambda x="Рваные раны":
                    self.set_reason_item(x),
        }
    ]

    self.menu = MDDropdownMenu(
        caller=self.ids.reason,
        items=self.menu_list,
        position="bottom",
        width_mult=4
    )
    self.menu.open()
