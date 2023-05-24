from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineAvatarListItem
from kivy.core.window import Window
from dropdown_modul.medical_care_provided_modul import (
    medical_care_provided_mod)

from config.getting_data_db import view_all_name
from create_qrcode.qrcode_make import make_qrcode
from button_press.button_on_click import on_click
from config.send_qr_date import qrcode_to_db_
from create_qrcode.read_qrocde import on_symbols_

from dropdown_modul.floor_menu import floor_mod
from dropdown_modul.affiliation_menu import affiliation_menu_mod
from dropdown_modul.military_rank_menu import military_rank_mod
from dropdown_modul.reason_for_the_appeal import reason_for_the_appeal_mod
from dropdown_modul.diagnosis_menu import diagnosis_mod
from dropdown_modul.voluntary_consent_menu import voluntary_consent_mod
from dropdown_modul.first_medical_aid import first_medical_aid_mod
from dropdown_modul.evacuation_menu import evacuation_mod
from dropdown_modul.evacuation_queue_menu import evacuation_queue_mod
from dropdown_modul.where_delivered_menu import where_delivered_mod
from dropdown_modul.evacuation_method_menu import evacuation_method_mod
from dropdown_modul.counter_menu import counter_mod
from file_kv import KV


Window.size = (500, 750)


class Item(OneLineAvatarListItem):
    """Класс для отображения иконок и текста в выпадающем меню"""
    divider = None
    source = StringProperty()


class FirstScreen(Screen):

    def set_item(self, text_item):
        """Метод для закрытия выпадающего меню"""
        self.screen.ids.drop_item.set_item(text_item)
        self.menu.dismiss()

    def transition_on_second_scr(self, text__item):
        """Переход на второй экран"""
        self.manager.current = 'second'
        self.menu.dismiss()

    def transition_on_make_qrcode_scr(self, text__item):
        """Переход на экран создания qr code"""
        self.manager.current = 'qrcode_screen'
        self.menu.dismiss()

    def transition_to_read_qrcode_scr(self, text__item):
        """Переход на экран считывания qr code"""
        self.manager.current = 'camera_click'
        self.menu.dismiss()

    def view_all(self):
        """Просмотр данных на главном экране"""
        return view_all_name(self)

    def button_press(self):
        """Создание qr code при нажатии на кнопку отправить"""
        return make_qrcode()


class SecondScreen(Screen):
    """ Второй экран приложения"""

    def document_number_tap(self):
        return counter_mod(self)

    def set_document_number_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.document_number.text = text__item
        self.menu.dismiss()

    def patients_gender(self):
        """Пол пациента"""
        return floor_mod(self)

    def set_floor_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.floor.text = text__item
        self.menu.dismiss()

    def affiliation_menu(self):
        """Принадлежность"""
        return affiliation_menu_mod(self)

    def set_affiliation_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.affiliation.text = text__item
        self.menu.dismiss()

    def military_rank(self):
        """Воинские звания"""
        return military_rank_mod(self)

    def set_military_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.rank.text = text__item
        self.menu.dismiss()

    def reason_for_the_appeal(self):
        """Причина обращения"""
        return reason_for_the_appeal_mod(self)

    def set_reason_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.reason.text = text__item
        self.menu.dismiss()

    def patients_diagnosis(self):
        """Диагноз"""
        return diagnosis_mod(self)

    def set_diagnosis_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.diagnosis.text = text__item
        self.menu.dismiss()

    def voluntary_consent_patients(self):
        """Информированиео добровольном согласии """
        return voluntary_consent_mod(self)

    def set_voluntary_consent_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.voluntary_consent.text = text__item
        self.menu.dismiss()

    def first_medical_aid(self):
        """Первая медицинская помощь"""
        return first_medical_aid_mod(self)

    def set_first_medical_aid_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.first_aid.text = text__item
        self.menu.dismiss()

    def medical_care_provided(self):
        """Оказанная медицинская помощь"""
        return medical_care_provided_mod(self)

    def set_item_medical(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.medical.text = text__item
        self.menu.dismiss()

    def evacuation_patients(self):
        """Эвакуация"""
        return evacuation_mod(self)

    def set_evacuation_medical(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.evacuation.text = text__item
        self.menu.dismiss()

    def evacuation_queue_patients(self):
        """Очередь эвакуации"""
        return evacuation_queue_mod(self)

    def set_evacuation_queue_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.evacuation_queue.text = text__item
        self.menu.dismiss()

    def evacuation_method_patients(self):
        """Куда доставлен пациент"""
        return evacuation_method_mod(self)

    def set_evacuation_method_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.evacuation_method.text = text__item
        self.menu.dismiss()

    def where_delivered_patients(self):
        """Куда доставлен пациент"""
        return where_delivered_mod(self)

    def set_where_delivered_item(self, text__item):
        """Метод для закрытия выпадающего меню"""
        self.ids.where_delivered.text = text__item
        self.menu.dismiss()

    def sand_date_to_db(self):  # Метод действие кнопки
        """Сохранение данных в csv и db"""
        return on_click(self)


class QR_CodeScreen(Screen):

    def view_image(self, root):
        self.ids.img_.source = 'static_fiels/site.png'


# Я не уверен, что нам это нужно, но я слишком сильно боюсь это удалять.
class CameraClick(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_symbols(self, instance, symbols):
        """Декодирование cq code"""
        return on_symbols_(self, instance, symbols)

    def put_db(self):
        """Добавление данных из qr coda в базу данных"""
        return qrcode_to_db_(self)


sm = ScreenManager()
sm.add_widget(FirstScreen(name='first'))
sm.add_widget(SecondScreen(name='second'))
sm.add_widget(QR_CodeScreen(name='qrcode_screen'))
sm.add_widget(CameraClick(name='camera_click'))


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.theme_cls.theme_style = "Dark"  # Тема основного приложения
        self.theme_cls.primary_palette = 'Red'  # Цвет кнопки(Элеметов)
        return self.screen


if __name__ == "__main__":
    MainApp().run()

