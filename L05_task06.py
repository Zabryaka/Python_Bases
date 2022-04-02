with open('text_6.txt', 'r', encoding='utf-8') as schedule:
    schedule = schedule.read().split('\n')
    sch = {}
    for j in range(0, len(schedule)):
        h_fin = []
        h_ini = schedule[j].split(':')[1].split()
        for i in range(0, len(h_ini)):
            h_mid = h_ini[i].split('(')
            if h_mid[0].isnumeric() is True:
                h_fin.append(h_mid[0])
        sch[schedule[j].split(':')[0]] = sum(list(map(int, h_fin)))
    print(sch)
