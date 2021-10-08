from functools import wraps

def val_checker(l_func):
    def _val_checker(func):

        @wraps(func)
        def wrapper(num):
            if l_func(num):
                print(func(num))                                                   # выводим результат работы функции
            else:
                raise ValueError(f'wrong val {num}')                               # иначе поднимаем исключение с числом 'num'

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3



try:
    a = calc_cube(5)
except (ValueError, TypeError) as err:                                             # если "строка" введена - то принимается исключение TypeError и через переменную err  выводим на print(err)
 print(err)