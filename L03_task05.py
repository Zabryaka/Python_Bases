def sum_numb(m):
    my_sum = 0
    while True:
        num = []
        mm = m.split('#')
        mmm = mm[0].split()
        for i in range(0, len(mmm)):
            if mmm[i].isnumeric() is True:
                num.append(mmm[i])
            else:
                continue
        my_sum_old = my_sum
        my_sum = my_sum + sum(list(map(int, num)))
        if m.find('#') == -1:
            print(f'({my_sum_old}) {my_sum}')
            m = input('Введите ещё один набор чисел через пробел для суммирования или # для выхода: ')
            continue
        else:
            print(f'Итоговая сумма: {my_sum}')
            break
    return my_sum


n = input('Введите набор целых положительных чисел через пробел: ')
sum_numb(n)
