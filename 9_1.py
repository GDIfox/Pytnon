import itertools         # набор полезных итераторов
import time

class TrafficLight:
    __color = [['red', [7, 31]], ['yellow', [2, 33]], ['green', [7, 32]], ['yellow', [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):            # itertools.cycle - возвращает по одному значению из последовательности, бесконечное число раз.
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
#                   \r возвращает курсор в начало строки(начало позиции)
            time.sleep(light[1][0])


trafficlight_1 = TrafficLight()
trafficlight_1.running()