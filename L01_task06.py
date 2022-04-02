a = float(input('Сколько километров вы пробежали в первый день? '))
while a <= 0:
    a = float(input('Сколько километров вы пробежали в первый день? '))
b = float(input('Введите желаемое число километров: '))
while b <= 0:
    b = float(input('Введите желаемое число километров: '))
Day = 1
# print('День     км')
# print(f'{Day:<8} {a:.3f}')
while True:
    if a >= b:
        print('Вы достигните желаемого результата на', Day, 'день!')
        break
    else:
        a = a * 1.1
        Day += 1
        # print(f'{Day:<8} {a:.3f}')
        continue
