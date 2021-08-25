from random import randint

with open('text5.txt', 'w+') as f:
    for _ in range(randint(10, 30)):
        f.write(f'{randint(1, 30)} ')
    f.seek(0)
    sum_num = map(int, f.read().split())
    print(sum(sum_num))
