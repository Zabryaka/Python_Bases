class Road:

    def __init__(self, le, wi):
        self._length = le
        self._width = wi

    def mass_all_road(self, mass=0, height=0):
        print(f'Для покрытия дороги длиной {self._length} м и шириной {self._width} м слоем в {height} см\n'
              f'с использованием асфальта массой {mass} кг на 1 кв.м. потребуется......\n'
              f'{mass * height * self._width * self._length / 1000} т асфальта.')


road = Road(5000, 20)
road.mass_all_road(25, 5)
