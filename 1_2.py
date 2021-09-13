data_cub = []
summa = 0

for x in range(1, 1000, 2):
    x_3 = x ** 3
    data_cub.append(x_3)

for index, znach in enumerate(data_cub):
    sum_x = 0
    while znach > 0:
        sum_x += znach % 10
        znach //= 10
    if sum_x % 7 == 0:
        summa += data_cub[index]
    data_cub[index] += 17

print(summa)

summa = 0

for index, znach in enumerate(data_cub):
    sum_x = 0
    while znach:
        sum_x += znach % 10
        znach //= 10
    if sum_x % 7 == 0:
        summa += data_cub[index]
print(summa)
