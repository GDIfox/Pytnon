class Stationery:                                                 # класс родителя
    def __init__(self, title='Something that can draw'):
        self.title = title                                        # при создании объекта передаем значение атрибуту

    def draw(self):
        print(f'Just start drawing! {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title} pen!')                    # подставляем значение pen = Pen('Parker')


class Pencil(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title} pencil!')


class Marker(Stationery):
    def draw(self):
        print(f'Start drawing with {self.title} marker!')


stat = Stationery()
pen = Pen('Parker')
pencil = Pencil('Faber-Castell')
marker = Marker('Copic')

office_supplines = [stat, pen, pencil, marker]

for i in office_supplines:
    i.draw()


