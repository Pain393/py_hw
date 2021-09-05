class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значение '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                if input(f'Введите "r", чтобы продолжить ввод ') == 'r':
                    print(err.my_input())
                else:
                    print(f'Итоговый список - {self.my_list}')
                    return f'Программа завершена.'

err = Error(1)
print(err.my_input())