data = []
fields = ['Имя', 'Фамилия', 'Год рождения', 'Город', 'Email', 'Телефон']


def conclusion(*args):
    for arg in args:
        data_str = ' '.join(arg)
        print(data_str)


def inp():
    for field in fields:
        person = input(f'{field}: ')
        data.append(person)
    conclusion(data)


inp()
