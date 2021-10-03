import os
import django
from collections import defaultdict

def dir_info():
    root_dir = django.__path__[0]  #файловая структура библ. django
#если ключ не найден в словаре, то вместо KeyError создается новая запись
    django_files = defaultdict(int)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))  # размер файла кратно 10. размер файла получаем из атрибута .st_size
            django_files[size] += 1  # суммируется количество

    for size, nums in serted(django_files.items()):   # сортируем по порядку
        print(f'{size}: {nums}')

dir_info()