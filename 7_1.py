# модуль для работы с операционной системой

import os

# необходимая структура папок
p_list = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'authapp': []}]}

# работа цикла возвращая объект вида , который отображает список (ключ, значение)
for key, value in p_list.items():
# True если путь относится к существующему пути. Возврат False за символические ссылки
    if not os.path.exists(key):
        for item in value:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))
