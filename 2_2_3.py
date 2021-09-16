spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for index, znach in enumerate(spisok):
    if znach.isdigit():
        spisok[index] = f'"{int(znach):02}"'
    elif znach[1:].isdigit():
        spisok[index] = f'"{znach[0]}{int(znach[1:]):02}"'

print(spisok)
print(' '.join(spisok))