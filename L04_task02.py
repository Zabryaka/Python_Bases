from random import randint

list_source = [randint(1, 333) for i in range(1, 14)]
print('Исходный список: ', list_source)
list_proc = [list_source[j] for j in range(1, len(list_source)) if list_source[j] > list_source[j - 1]]
print('Список из элементов, которые больше предыдущего: ', list_proc)
