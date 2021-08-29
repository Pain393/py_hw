class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return sum(self._income.values())


homer = Position('Гомер', 'Симпсон', 'Инженер', 3000, 500)
marge = Position('Мардж', 'Симпсон', 'Домохозяйка', 500, 100)

print(f'Зарплата сотрудника {homer.get_full_name()} с должностью {homer.position} составляет {homer.get_full_salary()} д.е.')
print(f'Зарплата сотрудника {marge.get_full_name()} с должностью {marge.position} составляет {marge.get_full_salary()} д.е.')
