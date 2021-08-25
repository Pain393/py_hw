'''Суть взял из интернета, задание сложноватое.
   Но разобрался в задаче, и это главное.     '''
my_dict = {}
with open('text6.txt', encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or ('0' <= i <= '9')]).split()))
        my_dict[name] = name_sum
    print(f'{my_dict}')
