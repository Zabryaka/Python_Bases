class MyDigitErr(Exception):

    def __init__(self, text):
        self.text = text


m = input("Введите целое положительное число: ")
my_num = []
while True:
    try:
        if m.isnumeric() is False:
            if m == '#':
                print(my_num)
                break
            raise MyDigitErr("Целое и положительное, Карл!")
    except MyDigitErr as err:
        print(err)
    else:
        my_num.append(int(m))
    m = input("Введите целое положительное число или # для выхода: ")
