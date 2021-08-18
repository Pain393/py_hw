def my_func(x, y):
    res = 1 / x
    for i in range(abs(y) - 1):
        res /= x
    print(f'Результат возведения в степень равен {res}')

my_func(2.13, -4)

# Хоть где-то пригодилось математическое образование