# choice - случайный элемент непустой последовательности
# randrange - (start, stop, step) - возвращает случ. выбранное число из последовательности

from random import choice, randrange


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def some_fun(n, repeat=False):      # repeat - флаг (по умолчанию)
# n - колчество шуток
# repeat - уникальные\неуникальные
# return - случайные шутки

    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy() #для работы с копиями, в случаях удаления значений
    spisok_of_j = []                                               # список дл ясложения
    spisok_min = min(no, adv, adj)             # для записи списка с минимальным количества элементов

    while n and len(spisok_min):            # пока есть значение n (кол. шуток) мы его будем уменьшать  (n -= 1) при условии НАЛИЧИЯ длинны минимального списка len(list(min))
        num = randrange(len(spisok_min))    # случайный индекс для вырезки значения (в диапазоне минимального списка)
        if repeat:
            spisok_of_j.append(f'{no.pop(num)} {adv.pop(num)} {adj.pop(num)}')   # удаляются элементы с помощью .pop() + возвращение эл-тов - подставляется в f'' строку и записывается .append в список (если ЕСТЬ ФЛАГ)
        else:
            spisok_of_j.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')  # если нет ФЛАГА! (использование choice без удаления списков)
        n -= 1           # итерация - шутка с формированна -> переходим к следующей
    return spisok_of_j     # завершение функции


print(some_fun(10, True))