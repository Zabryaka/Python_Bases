Phrase = input('Введите фразу из нескольких слов: ').split()
# print(Phrase)
for i, v in enumerate(Phrase):
    if len(Phrase[i]) > 10:
        print(f"{i + 1}) {v[0:10]}")
    else:
        print(f"{i + 1}) {v}")
