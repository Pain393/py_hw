class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_int(cls, string):
        my_date = []
        for i in string.split('-'):
            my_date.append(i)
        print(f'Дано:\n{int(my_date[0])} число\n{int(my_date[1])} месяц\n{int(my_date[2])} год')

    @staticmethod
    def date_valid(string):
        day, month, year = map(int, string.split('-'))
        if 1 <= day <= 31 and 1 <= month <= 12 and 0 < year < 10000:
            print('Введены верные данные')
        else:
            print('Введены НЕверные данные')


d = '26-11-1916'
Date.date_int(d)
Date.date_valid(d)
