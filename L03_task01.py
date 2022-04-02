def divide(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print('ERR!', 'Надо было вводить числа')
    else:
        try:
            div = num1 / num2
        except ZeroDivisionError as err:
            print('ERR!', err)
        else:
            if num1 % num2 == 0:
                return print(int(div))
            else:
                return print(div)


NUM1 = input('Делимое: ')
NUM2 = input('Делитель: ')
divide(NUM1, NUM2)
