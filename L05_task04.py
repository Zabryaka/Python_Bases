numbers = open('text_4.txt', 'r')
numbers_new = open('text_4_rus.txt', 'w', encoding='utf-8')

numbs = numbers.read().split('\n')
str1 = numbs[0].replace('One', "Один")
str2 = numbs[1].replace('Two', "Два")
str3 = numbs[2].replace('Three', "Три")
str4 = numbs[3].replace('Four', "Четыре")

numbers_new.write(f'{str1}\n{str2}\n{str3}\n{str4}\n')

numbers.close()
numbers_new.close()
