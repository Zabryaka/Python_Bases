from sys import argv

name, hours, sal, prem = argv
try:
    hours = float(hours)
    sal = float(sal)
    prem = float(prem)
except ValueError:
    print('Err! Вводите числа!')
else:
    money = hours * sal + prem
    print(money)
