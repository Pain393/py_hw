class OfficeEquipment:
    my_store = []

    def __init__(self, brand, price, quantity):
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Марка: {self.brand}\nЦена: {self.price}\nКоличество: {self.quantity}'

    def reception(self):
        if self.brand != 'Неизвестная марка' or self.price != 0 or self.quantity != 0:
            new = {'Марка': self.brand, 'Цена': self.price, 'Количество': self.quantity}
            self.my_store.append(new)
            print(f'Добавлено в склад:\n {self.my_store}')
        else:
            try:
                brand = input(f'\nВведите новую марку - ')
                price = int(input(f'Введите цену - '))
                quantity = int(input(f'Введите количество - '))
                new = {'Марка': brand, 'Цена': price, 'Количество': quantity}
                self.my_store.append(new)
                print(f'\033[1m\nТекущий склад:\033[0m\n {self.my_store}')
            except:
                print(f'Ошибка ввода данных, попробуйте еще раз!')
                return OfficeEquipment.reception(self)

            q = input(f'Для выхода нажмите "q", иначе что-нибудь другое - ')
            if q in ('Q', 'q', 'Й', 'й'):
                print('\033[1m\nВесь склад:\033[0m')
                for x in self.my_store:
                    print(x)
            else:
                return OfficeEquipment.reception(self)


class Printer(OfficeEquipment):
    def __init__(self, brand='Неизвестная марка', price=0, quantity=0, func='печать документов'):
        super().__init__(brand, price, quantity)
        self.func = func

    def to_print(self):
        return f'Функция устройства: {self.func}\n'


class Scanner(OfficeEquipment):
    def __init__(self, brand='Неизвестная марка', price=0, quantity=0, func='сканировать документы'):
        super().__init__(brand, price, quantity)
        self.func = func

    def scan(self):
        return f'Функция устройства: {self.func}\n'


class Copier(OfficeEquipment):
    def __init__(self, brand='Неизвестная марка', price=0, quantity=0, func_1='сканировать документы',
                 func_2='печать документов'):
        super().__init__(brand, price, quantity)
        self.func_1 = func_1
        self.func_2 = func_2

    def copy(self):
        return f'Функции устройства: {self.func_1}, {self.func_2}'


p = Printer('CANON', 6000, 3)
s = Scanner('EPSON', 2000, 2, 'подставка для чая')
c = Copier('XEROX', 10500, 5)
a = Printer()
p.reception()
s.reception()
c.reception()
a.reception()
print()
print(p, p.to_print(), sep='\n')
print(s, s.scan(), sep='\n')
print(c, c.copy(), sep='\n')
