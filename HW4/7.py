def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield i, res


try:
    n = int(input('Введите число и получите его факториал: '))
    for i, el in fact(n):
        print(f'{i}! = {el}')
except:
    print('Ну число же, попробуйте научиться соблюдать правила игры')
