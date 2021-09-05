class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + bi'

    def __add__(self, other):
        print(f'Сумма двух комплексных чисел равна')
        na = self.a + other.a
        nb = self.b + other.b
        if nb >= 0:
            return f'z = {na} + {nb}i'
        else:
            return f'z = {na} - {abs(nb)}i'

    def __mul__(self, other):
        print(f'Произведение двух комплексных чисел равно')
        na = self.a * other.a - self.b * other.b
        nb = self.b * other.a + self.a * other.b
        if nb >= 0:
            return f'z = {na} + {nb}i'
        else:
            return f'z = {na} - {abs(nb)}i'

    def __str__(self):
        if self.b >= 0:
            return f'Комплексное число {self.a} + {self.b}i'
        else:
            return f'Комплексное число {self.a} - {abs(self.b)}i'

z_1 = ComplexNumber(3, -5)
z_2 = ComplexNumber(10, 14)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)