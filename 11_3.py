class OnlyNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    my_word = input('Введите число чтобы продолжить, или stop, чтобы закончить: ')
    if my_word == 'stop':
        break
    else:
        try:
            if my_word.isdigit() is False:
                raise OnlyNumber('Вы ввели текст! Необходимо было ввести число!')
            else:
                my_list.append(int(my_word))
        except OnlyNumber as err:
            print(err)


print(my_list)