from functools import reduce


def func_multi(el1, el2):
    return el1 * el2


def fact(n):
    fact_list = []
    try:
        m = int(n)
    except ValueError:
        print('ERR: Вводите целое число')
    else:
        if m < 0:
            print('ERR: число должно быть положительным')
        elif m == 0:
            yield m
            print(f'0! равен 1')
        else:
            for i in range(1, m + 1):
                fact_list.append(i)
                yield i
            print(f'{m}! равен {reduce(func_multi, fact_list)}')


num = input('Введите целое положительное число: ')
fact(num)
for el in fact(num):
    print(el)
