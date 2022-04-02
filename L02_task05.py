rey = []
i = 0
Sol = input('Хотите ввести число? (Y/N) ')
while True:
    if Sol == 'Y' or Sol == 'y':
        num = int(input('Введите натуральное число: '))
        if i == 0:
            rey.insert(0, num)
            i += 1
            Sol = input('Хотите ввести ещё число? (Y/N) ')
            continue
        else:
            for j in range(0, len(rey)):
                if rey[j] < num:
                    rey.insert(j, num)
                    break
            if len(rey) < i + 1:
                rey.append(num)
            print(rey)
            i += 1
            Sol = input('Хотите ввести ещё число? (Y/N) ')
            continue
    else:
        break
print('Итоговый рейтинг: ', rey)
