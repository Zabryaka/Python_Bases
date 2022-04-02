Proceeds = float(input('Введите выручку фирмы (в рублях): '))
Costs = float(input('Введите издержки фирмы за тот же период (в рублях): '))
if Costs >= Proceeds:
    print('Фирма работает с убытком.')
else:
    print('Фирма работает с прибылью.')
    Profit = Proceeds / Costs
    print('Рентабельность выручки составляет:', f'{Profit:.2f}', 'руб.')
    Workers = int(input('Введите число работников фирмы: '))
    print('Прибыль фирмы на одного человека составляет:', f'{Profit / Workers:.2f}', 'руб.')
