a = float(input('Введите начальный результат спортсмена: '))
b = float(input('Введите конечный результат спортсмена: '))
i = 1
while a < b:
    a += a * 0.1
    i += 1
print(f'На {i}-й день спортсмен достиг результата — не менее {b} км.' )