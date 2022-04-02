class Matrix:

    def __init__(self, content):
        if type(content) == list:
            for i in range(0, len(content)):
                if type(content[i]) == list:
                    continue
                else:
                    print("Введен неверный формат данных!")
            self.content = content
        else:
            print("Введен неверный формат данных!")

    def __str__(self):
        m = []
        for j in range(0, len(self.content)):
            m.append(" ".join(list(map(str, self.content[j]))))
        return '\n'.join(m)

    def __add__(self, other):
        rez = []
        if len(self.content) != len(other.content):
            return f'Число строк матрицы должно быть одинаковым!'
        else:
            for i in range(len(self.content)):
                m = []
                if len(self.content[i]) != len(other.content[i]):
                    return f'Число столбцов матрицы должно быть одинаковым!'
                else:
                    for j in range(len(self.content[i])):
                        m.append(self.content[i][j] + other.content[i][j])
                    rez.append(m)
            return rez


pip1 = Matrix([[1, 2], [2, 3]])
pip2 = Matrix([[2, 3], [4, 5]])
print(pip1)
print(pip2)
print(pip1 + pip2)
