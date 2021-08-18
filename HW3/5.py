result = 0

while True:
    text = input('Числа: ')
    elements = text.split()
    for el in elements:
        if el == '!':
            print(f'Программа завершена, итоговая сумма: {result}')
            quit()
        else:
            try:
                result += int(el)
            except:
                print(f'Вы ввели неверные данные. Итоговая сумма: {result}')
                quit()
    print(result)
