num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_str = []
try:
    with open('text4.txt', encoding="utf-8") as f:
        with open('new_text4.txt', 'w', encoding="utf-8") as new_f:
            lines = f.readlines()
            for line in lines:
                line = line.split(' ', 1)
                new_str.append(num[line[0]] + ' ' + line[1])
            new_f.writelines(new_str)
except FileNotFoundError:
    print('Файл не найден.')
