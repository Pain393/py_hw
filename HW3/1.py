def division(a, b):
    if b == 0:
        print('На 0 делить нельзя, попробуйте другое число')
    else:
        print(a / b)

print('Введите два числа для нахождения их частного')
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
division(a, b)