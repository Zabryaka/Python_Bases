from itertools import cycle, count
from sys import argv


def int_start(x, y, z):
    """

    :param x: стартовое число списка
    :param y: конечное число списка
    :param z: сколько раз повторить список
    :return: список - int_list

    """
    int_list = []
    try:
        num_start = int(x)
        num_fin = int(y)
        num_times = int(z)
    except ValueError:
        print('ERR: Вводите целое число')
    else:
        for el in count(num_start):
            if el > num_fin:
                break
            else:
                # print(el)
                int_list.append(el)
        print(int_list)

        n = 1
        for ell in cycle(int_list):
            if n > num_times * len(int_list):
                break
            n += 1
            print(ell)

    return int_list


name, a, b, c = argv
int_start(a, b, c)
