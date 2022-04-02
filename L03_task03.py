def sum2max(num1, num2, num3):
    try:
        combo = [float(num1), float(num2), float(num3)]
    except ValueError as err:
        print(err)
        print('В следующий раз вводите числа :)')
    else:
        combo.remove(min(combo))
        sum2 = sum(combo)
        return f'Сумма двух максимальных чисел равна {sum2}'


NUM1 = input('Введите число (1 из 3): ')
NUM2 = input('Введите число (2 из 3): ')
NUM3 = input('Введите число (3 из 3): ')
print(sum2max(NUM1, NUM2, NUM3))
