class Stationary:

    def __init__(self, name='Канцелярская принадлежность'):
        self.title = name

    def draw(self):
        print(f"{self.title} что-то рисует или пишет.")


class Pen(Stationary):

    def draw(self):
        if self.title == 'Канцелярская принадлежность':
            self.title = 'Ручка'
        print(f"{self.title} аккуратно пишет буквы и цифры.")


class Pencil(Stationary):
    def draw(self):
        if self.title == 'Канцелярская принадлежность':
            self.title = 'Карандаш'
        print(f"{self.title} может нарисовать настоящий шедевр (цветной или черно-белый).")


class Handle(Stationary):
    def draw(self):
        if self.title == 'Канцелярская принадлежность':
            self.title = 'Маркер'
        print(f"{self.title} рисует жирненькие и яркии линии.")


Stationary().draw()
Pen().draw()
Pencil().draw()
Handle("Синий маркер").draw()
