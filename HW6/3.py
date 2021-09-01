class Cell:

    def __init__(self, num):
        self.num = int(num)

    def __add__(self, other):
        return f'Размер новой клетки после сложения двух других равен: {self.num + other.num}.'

    def __sub__(self, other):
        sub = self.num - other.num
        if sub > 0:
            return f'Размер новой клетки после вычитания одной клетки из другой равен: {sub}.'
        else:
            return 'Нельзя вычесть из меньшей клетки бОльшую.'

    def __mul__(self, other):
        return f'Размер новой клетки после умножения двух других равен: {self.num * other.num}.'

    def __truediv__(self, other):
        try:
            return f'Размер новой клетки после умножения двух других равен: {self.num // other.num}.'
        except ZeroDivisionError:
            return 'Нельзя делить на нулевую клетку'

    def make_order(self, row):
        result = ''
        for i in range(int(self.num / row)):
            result += '*' * row + '\n'
        result += '*' * (self.num % row) + '\n'
        return result


a = Cell(50)
b = Cell(40)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(15))