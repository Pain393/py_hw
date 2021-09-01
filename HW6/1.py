class Matrix:

    def __init__(self, mat):
        self.mat = mat

    def __str__(self):
        return '\n'.join(['\t'.join([str(el) for el in i]) for i in self.mat])

    def __add__(self, other):
        for i in range(len(self.mat)):
            for j in range(len(other.mat[i])):
                self.mat[i][j] = self.mat[i][j] + other.mat[i][j]
        return Matrix.__str__(self)


my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_matrix = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(f'Первая матрица:\n{my_matrix}')
print(f'Вторая матрица:\n{new_matrix}')
print(f'Сумма двух матриц:\n{my_matrix + new_matrix}')
