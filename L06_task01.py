from time import sleep


class TrafficLight:
    __color = 'Выключен'

    def running(self, cycles, green_time):
        i = 0
        while i < cycles:
            print('\r \033[31m Красный', end='')
            sleep(7)
            print('\r \033[33m Жёлтый', end='')
            sleep(2)
            print('\r \033[32m Зелёный', end='')
            sleep(green_time)
            print('\r \033[33m Жёлтый', end='')
            sleep(2)
            i += 1
        print(f'\r \033[0m {self.__color}')


TrafficLight().running(3, 10)
