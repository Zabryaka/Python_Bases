class MyErr(Exception):

    def __init__(self, text):
        self.text = text


a = input("Введите делимое: ")
b = input("Введите делитель, отличный от нуля: ")

try:
    aa = float(a)
    bb = float(b)
    if bb == 0:
        raise MyErr("Делитель не должен равняться нулю!")
except (ValueError, MyErr) as err:
    print(err)
else:
    print(f'{aa / bb:.3f}')
