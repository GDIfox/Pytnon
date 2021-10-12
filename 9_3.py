class Worker:                                                                    #родитель
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):                                                          # потомок
    def get_full_name(self):                                                     # соединяем name и surname. self - для привязки к конкретному объекту - 'manager'
        return f'{self.name} {self.surname}'

    def get_full_profit(self):                                                 # возвращение суммы значений wage и bonus
        return f'{sum(self._income.values())}'


manager = Position('Dorian', 'Grey', 'CEO', 500000, 125000)