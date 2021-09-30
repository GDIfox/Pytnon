# script_1

from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as babosiki:
    if 1 < len(argv) < 4 and [i for i in argv[1:] if i.isdigit()]:        # len(argv) - диапазон, ограничение значений 2 или 3, - [..] список нужен чтобы определить что ввели (для определения числа)
        if len(argv) == 3:
            start, finish = map(int, argv[1:])                            # с помощью map применяем int  к каждому эементу
            print(*(v for i, v in enumerate(babosiki) if start - 1 <= i < finish), sep='')    # происходит разбитие на start, finish
        else:
            print(*(v for i, v in enumerate(babosiki) if i >= int(argv[1]) - 1), sep='')      # здесь всего два элемента ( нет необходимотси start, finish)
    else:
        print(babosiki.read())

# script_2

from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as babosiki_1:
    with open('bakery.csv', 'r', encoding='utf-8') as babosiki_2:
        if len(argv) > 1 and [i for i in argv[1:] if '.' in i and i.replace('.', '').isdigit()]:
            if round(float(argv[1]), 3) <= 99999.99:                                                 # определение правильности диапазона (должны быть в условии диапазона)
                print(f"{round(float(argv[1]), 3):>010}", file=babosiki_1)                           # с помощью printa пишем file с условием числа не больше 10 позиций на результат
            else:
                print('Число должно быть меньше 99999.99')
        else:
            print(babosiki_2.read())