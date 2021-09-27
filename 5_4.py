src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#      300 не использовать - необходим сдвиг, т.к. возможна ошибка индексации

element = [src[znach] for znach in range(1, len(src)) if src[znach] > src[znach - 1]]
#                                     ^от 1 до длинны списка

print(element)