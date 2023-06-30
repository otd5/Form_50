main_dict = {

    'sex': {0: "Мужской", 1: "Женский"},

    'affiliation': {0: "Вооруженные силы", 1: "Гражданский персонал"},

    'military_rank': {0: "Рядовой", 1: "Ефрейтор", 2: "Младший сержант",
                      3: "Сержант", 4: "Старший сержант", 5: "Старшина",
                      6: "Прапорщик", 7: "Старший прапорщик", 8: "Лейтенант",
                      9: "Старший лейтенант", 10: "Капитан", 11: "Майор",
                      12: "Подполковник", 13: "Полковник", 14: "Генерал майор",
                      15: "Генерал лейтенант", 16: "Генерал полковник"
                      },
    
    'military_unit': {'0': '0'},

    'reason': {0: "Заболевание", 1: "Бытовая травма", 2: "Механическая травма",
               3: "Производственная травма", 4: "Огнестрельное ранение",
               5: "Осколочное ранение", 6: "Минно-взрывная травма",
               7: "Колотые проникающие раны",
               8: "Ожог", 9: "Рваные раны"
               },

    'diagnosis': {0: "Ранение", 2: "Отрыв конечности (какой)",
                  3: "Перевязывание", 4: "ДАТА и ВРЕМЯ",
                  5: "Медецинской помощи не потребовалось"},

    'voluntary': {0: "Согласен", 1: "Не согласен",
                  2: "Бессознательное состояние"},

    'first_medical': {0: "Оказана", 1: "Не оказана", 2: "Не требовалась"},

    'medical_care': {0: "Повязка на руку", 1: "Давящая повязка",
                     2: "Тампонада раны",
                     3: "Зажим (лигатура) на сосуд",
                     4: "Жгут, дата и время наложения", 5: "Контроль жгута",
                     6: "Очищение ротоглотки", 7: "Воздуховод", 
                     8: "Прошивание языка",
                     9: "ИВЛ", 10: "Ингаляция кислорода",
                     11: "Аспирация из трахеи",
                     12: "Конкотез иглами", 13: "Конкокритомия",
                     14: "Трахеостомия", 15: "Окклюзионная повязка",
                     16: "Выведение мочи", 17: "Антибиотк", 18: "Антитаксин",
                     19: "Сыворотка", 20: "Антидот"
                     },

    'evacuation': {0: "Сидя", 1: "Лежа"},

    'evacuation_queue': {0: "Первая", 1: "Вторая", 2: "Третья"},

    'evacuation_method': {0: "Автомобиль", 1: "Бронемашина", 2: "Спецборт"},

    'where_delivered': {0: "Мед. пункт", 1: "МОСН", 2: "Госпиталь"},

}


def decode_construct(line):
    new_line = line
    start_index = 3

    for key, value in main_dict.items():
        
        for element in line[start_index::]:
            if element in value.keys() or element == '':
                insert_index = line[start_index::].index(element) + start_index
                new_line.insert(insert_index, value.get(element))
                new_line.pop(insert_index+1)
                start_index += 1
                break
            else:
                start_index += 1
                break

    return new_line


def code_construct(line):
    new_line = list(line)

    for i in line:

        for j in main_dict.values():
            if i in j.values():

                for k, item in j.items():
                    if item == i:
                        new_line.insert(new_line.index(i), k)
                        new_line.pop(new_line.index(i))

    return new_line


def make_shorter(db_answer):
    new_list = []

    for line in db_answer:
        new_list.append(code_construct(line))

    return new_list


def decode_qrcode(qrcode_line):
    new_list = []

    for i in qrcode_line.split('\n'):
        if len(i) != 0:
            new_line = i.split(',')
            temp_line = []

            for element in new_line:
                if element.isdigit() is True:
                    element = int(element)
                    temp_line.append(element)

                else:
                    temp_line.append(element)

            new_list.append(decode_construct(temp_line))

    return new_list
