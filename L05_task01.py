some_str = open('text_01.txt', 'w', encoding='utf-8')

while True:
    str_str = input('Введите что-нибудь или #, когда надоест: ')
    if str_str == '#':
        break
    else:
        some_str.write(f'{str_str}\n')
        continue

some_str.close()
