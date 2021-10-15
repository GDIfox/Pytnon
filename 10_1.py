a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):     # преегрузка str
        return '\n'.join(map(str, self.lists))   # между списками в a и b добавляем \n - для вывода в print

    def __add__(self, other):       # суммируем матрицы между собой
        c = []
# из-за того что матрица содержита вложенные списки - используем два цикла для перебора данных
        for i in range(len(self.lists)):                 # рбота с 1-й матрицей
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])    # двойная индексация [i] - 0-й = [5, 3, 1, 6] - результат суммы складываем в подсписок c[i]
            return '\n'.join(map(str, c))     # возвращение не объект


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f'Matrix 1\n{matrix_1}\n{"-" * 20}')
print(f'Matrix 2\n{matrix_2}\n{"-" * 20}')
print(f'matrix 1 + matrix 2\n{matrix_1 + matrix_2}')
