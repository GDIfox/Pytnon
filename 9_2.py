class Road:
    def __init__(self, length, width):        # атрибуты: length (длина), width (ширина)
        self._length = length                 # защищенные атрибуты
        self._width = width                   # защищенные атрибуты

    def get_full_profit(self, weight=25, thickness=5):          # thickness - толщина асфальта
        return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см =" \
               f"{(self._length * self._width * weight * thickness) / 1000} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())       # если необходимо внести изменения, то вносим здесь road_1.get_full_profit(........) далее сразу подставляется в формулу return f".....