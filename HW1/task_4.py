chis = int(input('Введите  целое положительное число: '))
pr = -1
if chis > 0:
    while chis > 0:
        new_chis = chis % 10
        chis //= 10
        if new_chis > pr:
            pr = new_chis
    print(pr)
else:
    print('Вы ввели неподходящее число, повторите выполнение программы.')