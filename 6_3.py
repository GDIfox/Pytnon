from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as user:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        if len(user.readlines()) >= len(hobby.readlines()):                     # сравниваем длинну, readlines возвращает список,
            user.seek(0)
            hobby.seek(0)
            with open('dict_n_h.json', 'w', encoding='utf-8') as f:
                #       ^запись словаря
                all_list = zip_longest(('.'.join(us.split('.')) for us in user), hobby)                   # zip_longest объединяет между собой user и убираем запятую ("по феншую")
                my_dict = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}                     # записываем словарь, strip убирает пробелы и спец конструкции слева и справа (для вывода "по феншую")

                dump(my_dict, f, ensure_ascii=False, indent=4)
                #                ^из-за содержания кириллицы
                #                                     ^ отступы (форматирование вывода по "феншую")
            print(my_dict)
        else:
            exit(1)

