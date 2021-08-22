from itertools import count, cycle

c = 0
for i in count(int(input('Введите число: '))):
    print(i)
    if c == 5:
        break
    c += 1
# ----------------------------------------------
input('Нажмите Enter для выполнения второй программы')
count = 0
list = [1234, 'sdfsdf', '1232', 222, 213]
for i in cycle(list):
    if count == 15:
        break
    count += 1
    print(i)
