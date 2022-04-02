pip = open('text_02.txt', 'w+', encoding='utf-8')

pip.write(f'Вот это первая строка!\nА вот эта уже\nстала третья...\nНичего себе!!!\n')

pip.seek(0)

new_pip = pip.read().split('\n')
print(f'Количество строк в файле - {len(new_pip) - 1}')
for i in range(0, len(new_pip) - 1):
    print(f'Строка {i + 1}: "{new_pip[i]}" Слов в строке - {len(new_pip[i].split())}.')

pip.close()
