user_list = list(input('Введите любой набор символов, слово или словосочетание: '))

for i in range(1, len(user_list)):
    if i % 2 == 1:
        x = user_list[i - 1]
        user_list[i - 1] = user_list[i]
        user_list[i] = x
print(f"{'Туда:':<10}", user_list)

if len(user_list) % 2 == 0:
    user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
else:
    user_list[:len(user_list) - 1:2], user_list[1::2] = user_list[1::2], user_list[:len(user_list) - 1:2]
print(f"{'Обратно:':<10}", user_list)
