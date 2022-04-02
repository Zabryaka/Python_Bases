zabr_list = [True, 'Пора идти спать', 23, 243.4, 3 - 8j, complex(3, 5), (5, 6, 'абра-кадабра'), ['кортеж', 3], None,
             set('словечко'), {3: 'котик', 'keys': 22}]
for i in range(0, len(zabr_list)):
    print(f'{i:<4}', type(zabr_list[i]))
