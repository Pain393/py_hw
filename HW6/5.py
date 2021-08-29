class Stationery:
    def __init__(self):
        self.title = 'Начните рисовать прямо сейчас.'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f'У Вас в руках ручка. {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'У Вас в руках карандаш. {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'У Вас в руках маркер. {self.title}')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()