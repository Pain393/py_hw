sec_1 = int(input('Введите время в секундах: '))
min_1 = sec_1 // 60
hour_1 = min_1 // 60
min_2 = min_1 % 60
sec_2 = sec_1 % 60
print(f'Ваше введенное время в другом формате: {hour_1}:{min_2}:{sec_2}')