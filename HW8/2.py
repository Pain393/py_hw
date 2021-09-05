class Division:
    @classmethod
    def division(cls, a, b):
        try:
            print(f'Результат: {float(a) / float(b)}')
        except ZeroDivisionError:
            print('На 0 делить нельзя, попробуйте еще раз')
            cls.inp()
        except:
            print('Введены неверные данные, попробуйте еще раз')
            cls.inp()

    @classmethod
    def inp(cls):
        a = input('Введите первое число: ')
        b = input('Введите второе число: ')
        cls.division(a, b)


print('Введите два числа для нахождения их частного')
Division.inp()
