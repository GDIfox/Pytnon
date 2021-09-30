with open('load.txt', 'w', encoding='utf-8') as l:                                                 # загружаем(записываем) в файл результаты
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:                                       # считываем(работаем) с файлом
        info = (f"{line.split()[0]}, {line.split()[5][1:]}, {line.split()[6]}" for line in f)      # выбираем необходимые для работы элементы и обрабатываем
        for i in info:
            print(i, file=l)                                                                       # вывод(запись) результата в файл