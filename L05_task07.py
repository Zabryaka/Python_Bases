import json

with open('text_7.txt', 'r', encoding='utf-8') as firms_info:
    firms_info = firms_info.read().split('\n')
    firms = {}
    ave = []
    for j in range(0, len(firms_info)):
        delta = int(firms_info[j].split()[2]) - int(firms_info[j].split()[3])
        firms[firms_info[j].split()[0]] = delta
        if delta > 0:
            ave.append(delta)
    info = [firms, {"средняя прибыль": sum(ave) / len(ave)}]
    print(info)

with open('text_777.json', 'w+', encoding='utf-8') as krya:
    json.dump(info, krya, ensure_ascii=False)
    krya.seek(0)
    print(krya.read())
