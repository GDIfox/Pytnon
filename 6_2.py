import collections                                       # для оптимальной сортировки словаря по значению

with open('load.txt', 'r', encoding='utf-8') as l:       # открываем файл на чтение
    l_dict = collections.Counter()                       # создаем словарь

    for i in l:                                          # перебор элементов нашего файла
        i = i.split()[0]                                 # заменяем ip ключа
        l_dict[i] += 1

    ip, count = l_dict.most_common(1)[0][0], l_dict.most_common(1)[0][1]      # most_common возвращает список кортежей где сортировка поключами и работа с индексами
    print(f"spamer {ip} - {count} times")