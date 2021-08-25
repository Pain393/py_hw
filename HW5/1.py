with open('first.txt', 'a+') as f:
    while True:
        a = input()
        if a == '':
            break
        f.write(f'{a}\n')
    f.seek(0)
    for line in f:
        print(line, end='')
