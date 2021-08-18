vir = float(input('Введите выручку фирмы: '))
izd = float(input('Введите издержки фирмы: '))
if vir > izd:
    print('Фирма приносит прибыль')
    pr = vir - izd
    ren = pr / vir
    print(f'Рентабельность выручки {round(ren,2)}')
    sotr = int(input('Введите количество сотрудников фирмы: '))
    one_sotr = pr / sotr
    print(f'Прибыль фирмы на одного сотрудника в среднем: {round(one_sotr,2)} д.е.')
else:
    print('Фирма работает в убыток')