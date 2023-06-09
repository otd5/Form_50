KV = '''
#:import ZBarCam kivy_garden.zbarcam.ZBarCam
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol
#:import Snackbar kivymd.uix.snackbar.Snackbar

<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "20b2bd"
    text_color: "black"
    icon_color: "orange"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


ScreenManager:
    FirstScreen:
    SecondScreen:
    QR_CodeScreen:
    CameraClick:


<FirstScreen>:
 # Главный экран
    name: 'first'
    # toolbar: toolbar
    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    id: toolbar
                    right_action_items: [["static_fiels/1.png"]]
                    title: "Форма 50"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "20b2bd"
                    specific_text_color: "#fff0f5"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]

                MDLabel:
                    padding: [20, 20]
                    id: labled
                    font_style: 'H6'
                    text: "Cписок пациентов"
                    halign: "center"
                    text_color: "black"

                MDRectangleFlatIconButton:
                    text: 'Просмотреть всех пациентов'
                    heme_text_color: "Custom"
                    text_color: "black"
                    line_color: "20b2bd"
                    pos_hint: {'center_x': 0.7, 'center_y': .1}
                    on_press: root.view_all()


        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Меню"
                    title_color: "20b2bd"
                    text: "Форма 50"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                DrawerClickableItem:
                    icon: "hospital"
                    text_right_color: "#4a4939"
                    text: "Заполнение карты пациента"
                    # on_press: root.counter()
                    on_release: root.manager.current = 'second'

                DrawerClickableItem:
                    icon: "qrcode"
                    text_right_color: "#4a4939"
                    text: "Создать QR-сod"
                    on_press: root.button_press()
                    on_release:
                        root.manager.current = 'qrcode_screen'

                DrawerClickableItem:
                    icon: "qrcode-scan"
                    text_right_color: "#4a4939"
                    text: "Считываение QRCod"
                    on_release: root.manager.current = 'camera_click'

        # adaptive_size: False
        # orientation:"vertical"
        # size_hint: .6, .6
        # pos_hint: {"center_x": .5, "center_y": .5}
        # spacing: "10dp"


<SecondScreen>:
 # Заполнение карты пациента

    name: "second"
    surname: surname
    floor: floor
    affiliation: affiliation
    rank: rank
    reason: reason
    diagnosis: diagnosis
    voluntary_consent: voluntary_consent
    first_aid: first_aid
    evacuation: evacuation
    evacuation_queue: evacuation_queue
    where_delivered: where_delivered
    evacuation_method: evacuation_method
    document_number: document_number

    MDBoxLayout:
        adaptive_size: False
        orientation:"vertical"
        size_hint: .8, .9
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        spacing: "5dp"

        MDLabel:
            text: 'Внесите данные раненого бойца'
            halign: "center"


        ScrollView:
            bar_width: 0.4
            size_hint_y: 15
            pos_hint: {'center_y': .5}

            MDList:
                MDTextField:
                    id: document_number
                    hint_text: "Номер документа"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.document_number_tap()

                MDTextField:
                    id: surname
                    hint_text: "Ф.И.О"
                    color_mode: 'accent'
                    helper_text: "Поле для ручного ввода"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"

                MDTextField:
                    id: age
                    hint_text: "Возраст"
                    helper_text: "Возраст пациента"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"

                MDTextField:
                    id: floor
                    hint_text: "Пол"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.patients_gender()

                MDTextField:
                    id: affiliation
                    hint_text: "Принадлежность"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.affiliation_menu()

                MDTextField:
                    id: rank
                    hint_text: "Воинское звание"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.military_rank()

                MDTextField:
                    id: military_unit
                    hint_text: "Воинская часть/Наименование"
                    helper_text: "Поле для ручного ввода"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"

                MDTextField:
                    id: reason
                    hint_text: "Причина обращения"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.reason_for_the_appeal()

                MDTextField:
                    id: diagnosis
                    hint_text: "Диагноз"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    on_focus: if self.focus: root.patients_diagnosis()

                MDTextField:
                    id: voluntary_consent
                    hint_text: "Информированное добровольное согласие"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.voluntary_consent_patients()

                MDTextField:
                    id: first_aid
                    hint_text: "Первая помощь"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.first_medical_aid()

                MDTextField:
                    id: medical
                    hint_text: "Медицинская помощь"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.medical_care_provided()

                MDTextField:
                    id: evacuation
                    hint_text: "Эвакуация"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.evacuation_patients()

                MDTextField:
                    id: evacuation_queue
                    hint_text: "Очередь эвакуации"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.evacuation_queue_patients()

                MDTextField:
                    id: evacuation_method
                    hint_text: "Способ эвакуации"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.evacuation_method_patients()

                MDTextField:
                    id: where_delivered
                    hint_text: "Куда доставлен"
                    helper_text: "Выбрать из выпадающего списка"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"
                    readonly: True
                    on_focus: if self.focus: root.where_delivered_patients()

                MDTextField:
                    id: name_doctor
                    hint_text: "Ф.И.О Врача"
                    helper_text: "Данные заполнявшего форму"
                    helper_text_mode: "on_focus"
                    line_color_focus: "20b2bd"

        MDRectangleFlatIconButton:
            text: 'Отправить'
            heme_text_color: "Custom"
            text_color: "black"
            line_color: "20b2bd"
            pos_hint: {'center_x': 0.9, 'center_y': 0.5}
            on_press: root.sand_date_to_db()
            on_release: Snackbar(text="Данные успешно отправлены").open()

        MDRectangleFlatIconButton:
            text: '     Назад     '
            heme_text_color: "Custom"
            text_color: "black"
            line_color: "20b2bd"
            pos_hint: {'center_x': 0.9, 'center_y': 0.5}
            on_press: root.manager.current = 'first'




<QR_CodeScreen>:
 # Создание QR_code

    name:"qrcode_screen"
    MDBoxLayout:
        size_hint_y: .6
        pos_hint: {'center_y': .5}
        padding: 10
        Image:
            id: img_

    MDLabel:
        text: "QR Code"
        font_style: 'H4'
        pos_hint: {'center_y':.9}
        halign: 'center'

    MDBoxLayout:
        adaptive_size: True
        orientation:"vertical"
        size_hint: .5, .5
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        spacing: "5dp"


        MDRectangleFlatIconButton:
            text: 'Просмотреть QR Code'
            heme_text_color: "Custom"
            text_color: "black"
            line_color: "20b2bd"
            pos_hint: {'center_x': 0.9, 'center_y': 0.3}
            on_release: root.view_image(root)

        MDRectangleFlatIconButton:
            text: '     Назад     '
            theme_text_color: "Custom"
            text_color: "black"
            line_color: "20b2bd"
            pos_hint: {'center_x': 0.9, 'center_y': 0.5}
            on_press: root.manager.current = 'first'




<CameraClick>:
 # Считывание QR_code

    name: 'camera_click'
    MDBoxLayout:
        orientation:'vertical'
        size_hint: .9, .9
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        spacing: "5dp"
        ZBarCam:
            id:zbarcam
            code_types:ZBarSymbol.QRCODE.value,ZBarSymbol.EAN13.value
            on_symbols:root.on_symbols(*args)

        MDRectangleFlatIconButton:
            text: 'Отправить'
            theme_text_color: "Custom"
            line_color: "20b2bd"
            pos_hint: {'center_x': 0.9, 'center_y': 0.3}
            on_press: root.put_db()
            on_release: Snackbar(text="Данные сохранены").open()


        MDRectangleFlatIconButton:
            text: '     Назад     '
            theme_text_color: "Custom"
            text_color: "black"
            line_color: "20b2bd"
            pos_hint: {'center_x': 0.9, 'center_y': 0.3}
            on_press: root.manager.current = 'first'



'''
