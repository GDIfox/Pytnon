class Cell:
    def __init__(self, nums):
        self.nums = nums     # 13 ячеек

    def make_order(self, rows):      # разделить по 5 в ряд
        return '\n'.join(['kletka' * rows for _ in range(self.nums // rows)]) + '\n' + 'kletka' * (self.nums % rows)    # учитываем целочисленное деление и остаток от деления (кратное - ['kletka' * rows for _ in range(self.nums // rows)]
    # 'kletka' * rows - слово состоит из 5 символов и вычисляем сколько рядов получится (range(self.nums // rows)])) - целочисленное деление '\n' - переводим курсор ниже

    def __str__(self):                                    # возвращаем строковое представление объекта
        return f'{self.nums}'

    def __add__(self, other):                             # сложение
        print('Sum of cell is: ')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):                              # вычитание
        print('Subtraction of cell is: ')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше второй, вычитание не возможно.'

    def __mul__(self, other):                              # умножение
        print('Multiply of cell is: ')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):                        # целочисленное деление
        print('Truediv of cell is: ')
        return Cell(self.nums // other.nums)


cell_1 = Cell(15)
cell_2 = Cell(24)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)

