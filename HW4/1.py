from sys import argv


def salary():
    try:
        hours, rate, premium = map(float, argv[1:])
        print(f'Зарплата сотрудника: {hours * rate + premium} д.е.')
    except ValueError:
        print('Вы ввели совсем не то, попробуйте еще раз')
        salary()

salary()