class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'оклад': wage, 'премия': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}")

    def get_total_income(self):
        try:
            print(f"Доход с учётом премии: {float(self.income['оклад']) + float(self.income['премия'])} тугр.")
        except ValueError:
            print('Вводите зарплату в числах')


n = input("Введите имя... ")
s = input("Введите фамилию... ")
p = input("Введите должность... ")
w = input("Введите оклад (тугр.)... ")
b = input("Введите премию (тугр.)... ")
worker = Position(n, s, p, w, b)
worker.get_full_name()
worker.get_total_income()
