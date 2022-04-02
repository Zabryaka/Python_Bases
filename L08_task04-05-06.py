class Store:

    def add_to_store(self, store, n, obj):
        store[n] = obj
        return store

    def sent_to_smwh(self, buy_buy, dep, store, key):
        try:
            buy_buy[key] = [dep, store[key]]
            store.pop(key)
        except KeyError:
            print("\033[31m\033[1m{}\033[0m".format('Нет такой позиции на складе'))
        return buy_buy, store


class Equipment(Store):

    def __init__(self, name, number):
        self.name = name
        self.number = number


class Printer(Equipment):

    def __init__(self, name, number, pages):
        Equipment.__init__(self, name, number)
        self.pages = pages

    @property
    def show_info(self):
        return f'принтер {self.name}, {self.number} шт., {self.pages} стр.'

    @property
    def get_list(self):
        list_printer = ['принтер', self.name, self.number, self.pages]
        return list_printer


class Scanner(Equipment):

    def __init__(self, name, number, velocity):
        Equipment.__init__(self, name, number)
        self.velocity = velocity

    @property
    def show_info(self):
        return f'сканер {self.name}, {self.number} шт., {self.velocity} стр./мин.'

    @property
    def get_list(self):
        list_scanner = ['сканер', self.name, self.number, self.velocity]
        return list_scanner


class Xerox(Equipment):

    def __init__(self, name, number, pages, velocity):
        Equipment.__init__(self, name, number)
        self.pages = pages
        self.velocity = velocity

    @property
    def show_info(self):
        return f'ксерокс {self.name}, {self.number} шт., {self.pages} стр., {self.velocity} стр./мин.'

    @property
    def get_list(self):
        list_xerox = ['ксерокс', self.name, self.number, self.pages, self.velocity]
        return list_xerox


store = {}
buy_buy = {}
n = 1

while True:
    start = input('Будете вводить оборудование? Нажмите Enter для продолжения или # для выхода: ')
    if start == '#':
        break
    else:
        while True:
            type = input('1 - принтер, 2 - сканер, 3 - ксерокс: ')
            name = input('Название: ')
            number = input('Количество (шт.): ')
            try:
                type = int(type)
                if type == 1:
                    pages = input('Ресурс печати (кол-во стр.): ')
                    obj = Printer(name, number, pages)
                    break
                elif type == 2:
                    velocity = input('Скорость сканирования (стр./мин.): ')
                    obj = Scanner(name, number, velocity)
                    break
                elif type == 3:
                    pages = input('Ресурс печати (кол-во стр.): ')
                    velocity = input('Скорость сканирования (стр./мин.): ')
                    obj = Xerox(name, number, pages, velocity)
                    break
                else:
                    print('ERR: Введено неверное значение')
                    continue
            except ValueError:
                print('ERR: Введено неверное значение')
                continue
        print(obj.show_info)
        Store().add_to_store(store, n, obj.get_list)
        n += 1
print("\033[31m\033[1m{}\033[0m\n{}".format('Сейчас на складе: ', store))

while True:
    finish = input('Будете передавать оборудование? Нажмите Enter для продолжения или # для выхода: ')
    if finish == '#':
        break
    else:
        dep = input('Куда будем передавать?\n1 - бухгалтерия, 2 - IT, 3 - охрана: ')
        if int(dep) == 1:
            dep = 'бухгалтерия'
        elif int(dep) == 2:
            dep = 'IT'
        elif int(dep) == 3:
            dep = 'охрана'
        else:
            print('Нет такого подразделения')
            break
        key = int(input('Выберете номер позиции, имеющейся на складе: '))
        Store().sent_to_smwh(buy_buy, dep, store, key)
        print(f'Уехало со склада \n{buy_buy}')
        print("\033[31m\033[1m{}\033[0m\n{}".format('Осталось на складе: ', store))
        continue
