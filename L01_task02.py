Sec = int(input('Введите время в секундах: '))
H = Sec // 3600
M = (Sec - H * 3600) // 60
S = Sec - H * 3600 - M * 60
print('Точное время %.2d : %.2d : %.2d' % (H, M, S))
