stroka = input('Введите предложение: \n')
n = 0
for i in stroka.split():
    n += 1
    print(f'{n}. {i[:10]}')
