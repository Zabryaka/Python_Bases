class Cell:

    def __init__(self, numbs):
        self.numbs = numbs

    def __add__(self, other):
        return self.numbs + other.numbs

    def __sub__(self, other):
        if self.numbs > other.numbs:
            return self.numbs - other.numbs
        else:
            return f"Для вычитания в первой клетке должно быть больше ячеек, чем во второй!"

    def __mul__(self, other):
        return self.numbs * other.numbs

    def __truediv__(self, other):
        if self.numbs // other.numbs == 0:
            return f"Клетка не может поделиться!"
        else:
            return self.numbs // other.numbs

    def make_order(self, row):
        str_numb = self.numbs // row
        str_last = self.numbs % row
        str = f"{'*' * row}\n"
        print(f"{str * str_numb}{'*' * str_last}")


a = Cell(20)
b = Cell(2)
print(a + b)
print(b - a)
print(a - b)
print(a * b)
print(b / a)
print(a / b)
a.make_order(6)
