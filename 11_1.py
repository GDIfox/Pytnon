
class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def extract(cls, param):
        my_day, my_month, my_year = map(int, param.split('-'))
        return print(f"Дата: День - {my_day}, Месяц - {my_month}, Год - {my_year}")


    @staticmethod
    def validation(param):
        my_day, my_month, my_year = map(int, param.split('-'))
        if my_year % 4 == 0 and my_month == 2 and 0 < my_day <= 29:
            print(f'{param} - Високосный год')
        elif 0 < my_day <= 31 and 0 < my_month <= 12 and my_month != 2:
            print(f'{param} Год не високосный')
        else:
            print('Неверная дата')



my_calendar = input('Введите дату через "-" например 00-00-0000: ')
my_data = Data(my_calendar)
my_data.extract(my_calendar)
my_data.validation(my_calendar)