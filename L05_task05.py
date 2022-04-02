summary_rpt = open('text_05.txt', 'w+')

summary_rpt.write(f"{input('Введите набор числе, разделённых пробелами: ')}\n")
summary_rpt.seek(0)
try:
    print(sum(list(map(float, summary_rpt.read().split()))))
except ValueError:
    print("В следующий раз вводие числа!")

summary_rpt.close()

# ------------------------------------вариант----------------------------------------

summary = open('text_05.txt', 'a')

nms = input('Введите набор числе, разделённых пробелами: ')
try:
    nms_new = list(map(float, nms.split()))
except ValueError:
    print("В следующий раз вводие числа!")
else:
    print(sum(nms_new))
    summary.write(f'{nms}\n')

summary.close()
