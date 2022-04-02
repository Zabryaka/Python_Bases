def poly(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError as err:
        print(err)
        print('Вы ввели не те числа. Или не совсем числа. :)')
        return
    else:
        if x <= 0 or y >= 0:
            print('x должен быть больше 0, а y - меньше. Будьте внимательнее!')
            return
        else:
            # poly_rez = 1 / (x ** abs(y))
            xx = x
            for i in range(1, abs(y)):
                x = xx * x
                i += 1
            poly_rez = 1 / x
            return f'{xx} в степени {y} = {poly_rez}'


X = input('Введите действительное положительное число: ')
Y = input('Введите целое отрицательное число: ')
print(poly(X, Y))
