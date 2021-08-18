data = []


def my_func(*args):
    result = sum(args) - min(args)
    print(f'Сумма двух максимальных чисел равна {result}')


def inp():
    try:
        for i in range(3):
            data.append(int(input(f'Введите {i + 1} натуральное число: ')))
        my_func(data[0], data[1], data[2])
    except:
        print('Вы не соблюдаете правила, попробуйте еще раз!')
        data.clear()
        inp()

inp()
