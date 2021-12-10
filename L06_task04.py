class Car:

    def __init__(self, s, c, n, p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = bool(p)
        if self.is_police is True:
            print(f'Для законного управления этим автомобилем убедитесь, что вы сотрудник полиции.')

    def go(self):
        print(f'Полный вперёд!!!')

    def stop(self):
        print(f'Стоп машина!')

    def turn(self, direction):
        print(f'Поворачиваем {direction}.')

    def show_speed(self):
        print(f'Скорость автомобиля составляет {self.speed} км/ч.')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Вы превысили скорость! Ваша скорость составляет {self.speed} км/ч '
                  f'при максимально разрешённой 60 км/ч!')
        else:
            print(f'Скорость автомобиля составляет {self.speed} км/ч.')


class SportCar(Car):

    def stop(self):
        print(f'У спортивной машины нет педали тормоза!')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Вы превысили скорость! Ваша скорость составляет {self.speed} км/ч '
                  f'при максимально разрешённой 40 км/ч!')
        else:
            print(f'Скорость автомобиля составляет {self.speed} км/ч.')


class PoliceCar(Car):

    def go(self):
        print(f'В погоню за преступниками!!! Всем уступить дорогу! Виу-виу!')


Car(80, 'Синий', "Лада", 0).turn('налево')
SportCar(100, 'Красный', "Субару", 0).stop()
WorkCar(60, 'Black', "Mazda", 1).show_speed()
PoliceCar(90, 'Белый', "Порше", 1).go()
print(TownCar(40, 'Желтый', "Жигуль", 0).name)
