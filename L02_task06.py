goods = []
i = 0
answer = 'Да'
while True:
    if answer == 'Да' or answer == 'да':
        i += 1
        name = input(f'Введите название товара номер {i}: ')
        price = float(input(f'Введите цену товара номер {i} (в тугриках): '))
        amount = int(input(f'Введите количество товара номер {i}: '))
        units = input(f'В каких единицах измерения количество товара номер {i}? ')
        product = {"Название": name, "Цена": price, "Количество": amount, "Единицы измерения": units}
        pre_goods = (i, product)
        goods.append(pre_goods)
        answer = input('Хотите ввести информацию ещё об одном товаре? (Да/Нет) ')
    else:
        break
# print(goods)
Name = []
Price = []
Amount = []
Units = []
for j in range(0, len(goods)):
    Name_new = goods[j][1]['Название']
    Name.append(Name_new)
    Price_new = goods[j][1]['Цена']
    Price.append(Price_new)
    Amount_new = goods[j][1]['Количество']
    Amount.append(Amount_new)
    Units_new = goods[j][1]['Единицы измерения']
    Units.append(Units_new)
GOODS = {'Название': Name, "Цена": Price, "Количество": Amount, "Единицы измерения": Units}
print('Вы ввели следующие товары: ')
print(GOODS)
