N = int(input('Введите целое положительное число: '))
if N > 0:
    Rest = N // 10
    End = N - Rest * 10
    while Rest > 0:
        End2 = Rest - (Rest // 10) * 10
        Rest = Rest // 10
        if End2 > End:
            End = End2
        else:
            continue
    print('Самая большая цифра в числе: ', End)
else:
    print('Ошибка! Число должно быть положительным!')
