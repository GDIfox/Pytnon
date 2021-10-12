from random import choice             # для возврата случайного элемента из указанной последовательности

class Car:
    direction = ['north', 'north-east', 'east', 'south-east', 'south', 'south-west', 'west', 'north-west']   # напрвление движения автомобиля

    def __init__(self, n, c, s, p=False):                                # для оптимизации задачи, т.к. большинство авто не полицейские (исключем возможность постоянного прописывания в объекте p=False)
        self.name = n
        self.color = c                                                          # color и speed - не задаем случайно! получают значения при создании объекта!
        self.speed = s
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs the car a palice car? {p}')     #для вывода основных элементов как color и a palice car?

    def go(self):
        print(f'{self.name}: Car went.')

    def stop(self):
        print(f'{self.name}: Car stopped!')

    def turn(self):                                                          # направление поворота автомобиля
        print(f'{self.name}: Car turned {choice(self.direction)}.')          # какой автомобиль (name) - куда повернет (случайное значение из direction с помощью модуля choice)

    def show_speed(self):                                                    # cкорость автомобиля
        return f'{self.name}: Car speed: {self.speed}.'


class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 60 else super().show_speed()
#        если speed > 60 то такая-то машина name со скоростью speed. Speeding - это превышение (иначе вывести - f'{self.name}: Car speed: {self.speed}.' - чтобы это не дублировать используем - super().show_speed()!!!!)

class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding!' if self.speed > 40 else super().show_speed()

class SportCar(Car):
    '''sportcar'''

class PoliceCar(Car):

    def __init__(self, n, c, s, p=True):
        super().__init__(n, c, s, p)


police_car = PoliceCar('"Полицейский бронивечок"', 'серо-буро-малиновый', 80)
work_car = WorkCar('"Газелька"', ',бело-серая', 40)
sport_car = SportCar('"Ферари"', 'оранжевый', 120)
town_car = TownCar('"такси"', 'желтый', 65)
# создаем обекты для каждогно из классов

list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    i.go()                            # поехали
    print(i.show_speed())
    i.turn()                          # повернули
    i.stop()                          # остановились
    print()