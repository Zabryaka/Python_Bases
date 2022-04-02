sal = open('text_3.txt', 'r', encoding='utf-8')

sal_list = sal.read().split('\n')
surname = []
money = []
low = []
for i in range(0, len(sal_list)):
    surname.append(sal_list[i].split()[0])
    money.append(sal_list[i].split()[1])
    if float(money[i]) < 20000:
        low.append(surname[i])

print(f'Средняя зарплата составляет {sum(map(float, money))/len(money):.2f} тугр.')
print('Сотрудники с зарплатой менее 20 000 тург.:')
for i, v in enumerate(low, 1):
    print(f'{i}) {v}')

sal.close()
