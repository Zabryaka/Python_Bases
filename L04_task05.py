from functools import reduce


def func_multi(el1, el2):
    return el1 * el2


my_l = [el for el in range(100, 1001) if el % 2 == 0]
print(my_l)
print(reduce(func_multi, my_l))
