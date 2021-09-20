#w = ['Иван', 'Мария', 'Петр', 'Илья', 'Марина', 'Алина', 'Бибочка']


def thesaurus(*args):
    dictionary = {}
    for i in sorted(args):
        simbol = i[0]
        if simbol in dictionary:
            dictionary[simbol] += [i]
        else:
            dictionary[simbol] = [i]

    return dictionary


print(thesaurus('Бобр', 'Елена', 'Павел', 'Борис', 'Илья', 'Елизавета', 'Виктория', ))