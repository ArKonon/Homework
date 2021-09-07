class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print (f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        Stationery.draw(self)
        return f'{self.title} предназначена для записи'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        Stationery.draw(self)
        return f'{self.title} предназначен для черчения'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        Stationery.draw(self)
        return f'{self.title} предназначен для выделения текста'


pen = Pen('Ручка')
print(pen.draw())
pensil = Pencil('Карандаш')
print(pensil.draw())
handle = Handle('Маркер')
print(handle.draw())