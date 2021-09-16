many_many = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

# A)
for index in many_many:
    rub, kop = int(index // 1), int(f'{index % 1:.02f}'[2:])
    print(f'{rub} руб {kop:02d} коп,', end='')
    pass
# B)
print(f'\n')

print(f'ID base: {id(many_many)} - {many_many}')
many_many.sort()
print(f'ID change: {id(many_many)} - {many_many}')

# C_D)
print(f'\n')

many_list = sorted(many_many, reverse=True)
print(f'ID change: {id(many_list)} - {many_list}\n{many_list[:5][::-1]}')

