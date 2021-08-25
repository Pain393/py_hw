with open('second.txt') as f:
    content = f.readlines()
    num = len(content)
    print(f'Всего в файле {num} строк.')
    for i in range(num):
        print(f'Количество слов в {i + 1}-ой строке: {len(content[i].split())}.')
