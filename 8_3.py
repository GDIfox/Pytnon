from functools import wraps


def type_logger(func):                                                           # у декоратора аргуметом выступает - локальная функция - wrapper
    @wraps(func)
    def wrapper(*args, **kwargs):                                                       # некоторое количество позициооных и  именнованных аргументов (которые мы передаем в calc_cube)
        num_list = [el for el in (*args, *kwargs.values())]                        # подготовка информации ддля работы в 'n' (в num_list запаковываются данные a=calc_cube)
        n = [f'{func.__name__}({el}: {type(el)})' for el in num_list]              # формируем строки
        print(*n, *func(*args, **kwargs), sep=',\n')                               # выводим список 'n', распаковываем функцию, переносим строки

    return wrapper


@type_logger                                                                             # после обращения к фукции calc_cube - начинатеся работа декоратора type_logger(func)
def calc_cube(*x, **y):
    num_list = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]     # берем каждый элемент только если тип соответсвует возможности (int и float) для возведения в "куб"
    return [i ** 3 for i in num_list]


a = calc_cube(5, 11, 8.9, 34, vi=89.8, io=6)
print(calc_cube.__name__)
help(calc_cube)