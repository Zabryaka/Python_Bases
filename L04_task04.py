from random import randint

list_source = [randint(1, 30) for i in range(1, 20)]
list_pure = [el for el in list_source if list_source.count(el) == 1]
print('Случайный список: ', list_source)
print('Уникальные цифры: ', list_pure)
