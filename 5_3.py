from itertools import islice, zip_longest
#   ^сборник полезных итераторов
#                    ^итератор состоящий из среза
#                              ^создает итератор, кот.  объединяет элементы из каждой итерируемой последовательности в кортежи, в случае отстут.элемента - дополняет его.

t = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Мавританец', 'Кирилец']
k = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

#rezult = (i for i in zip_longest(t, k) if len(t) > len(k))
rezult = ((x, y) for x, y in zip_longest(t, k))

print(type(rezult), *rezult, sep='\n')
print(next(rezult)) #проверка, что исчерпался список
# print(type(rezult))
# print(*islice(rezult, 9))
# print(list(islice(rezult, 3))) # подтверждения того что список исчерпался