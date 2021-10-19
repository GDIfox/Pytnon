class CunningFox(Exception):
    def __init__(self, txt):
        self.txt = txt


my_num_1 = int(input('Введите число : '))
my_num_2 = int(input('Введите второе число : '))
try:
    if my_num_2 == 0:
        raise CunningFox('На ноль делить категорически нельзя!!!')
except CunningFox as err:
    print(err)
else:
    print(round(my_num_1 / my_num_2))
