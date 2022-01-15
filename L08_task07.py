class ComplexNums:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        if self.y == 0:
            return f'{self.x:.3f}'
        elif self.y > 0:
            return f'{self.x:.3f} + {self.y:.3f}j'
        else:
            return f'{self.x:.3f} - {abs(self.y):.3f}j'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return ComplexNums(new_x, new_y)

    def __mul__(self, other):
        new_x = self.x * other.x - self.y * other.y
        new_y = self.x * other.y + other.x * self.y
        return ComplexNums(new_x, new_y)


n1 = ComplexNums(0.3, 0)
n2 = ComplexNums(3, -9)
print(n1)
print(n2)
print(n1 + n2)
print(n1 * n2)
