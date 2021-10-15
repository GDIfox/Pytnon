from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod       # интерфейс
    def consumption(self):     # учет расхода ткани
        pass

    def __add__(self, other):                     # перегруженный метод
        Clothes.result += self.consumption + other.consumption
        return Costume(0)                  # объект класса ostume со знаечением 0

    def __str__(self):                           # перегруженный метод (сработает после окончательного суммирования)
        res = Clothes.result                     #
        Clothes.result = 0
        return f'{res}'


class Coat(Clothes):         # потомок
    @property           # интерфейс
    def consumption(self):
        return round(self.param / 6.5) + 0.5                    # получаем значения для последующих вычислений(


class Costume(Clothes):       # потомок
    @property
    def consumption(self):
        return round(2 * self.param + 0.3) / 100    #(подставляем Costume(0)=0 - в итоге опосле округления получаем тоже 0)


coat = Coat(42)
costume = Costume(170)
print(coat + costume + coat)