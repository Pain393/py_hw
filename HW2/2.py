n = int(input('Введите размер списка: '))
li = []

for num in range(n):
    a = input(f'Введите значение {num+1}: ')
    li.append(a)

print(li)
j = 0

for i in range(int(n / 2)):
    li[j], li[j + 1] = li[j + 1], li[j]
    j += 2

print(li)