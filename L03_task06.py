def int_func(xx):
    xxx = xx.split(' ')
    for j in range(0, len(xxx)):
        if bool(xxx[j]) is False:
            print('Упс! Кажется, вы ввели слишком много пробелов.')
            return
        else:
            continue
    x = ''.join(xxx)
    for i in range(0, len(x)):
        if ord(x[i]) < 97 or ord(x[i]) > 122:
            print('ERROR: Кажется, в вашем слове есть что-то помимо маленьких латинских букв.')
            return
        else:
            continue
    cap = xx.title()
    return print(cap)


X = input('Введите одно слово, состоящее из маленьких латинских букв: ')
int_func(X)

Y = input('А теперь введите несколько аналогичных слов через пробел: ')
int_func(Y)
