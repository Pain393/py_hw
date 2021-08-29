class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Данные авто: {self.name}, цвет {self.color}, скорость {self.speed} км/ч')

    def go(self):
        return f'Автомобиль {self.name} поехал со скоростью {self.speed} км/ч'

    def stop(self):
        self.speed = 0
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction):
        if direction not in ('налево', 'направо'):
            print(f'"{direction}" - неправильные данные.')
        else:
            self.direction = direction
            return f'Автомобиль {self.name} повернул {self.direction}'

    def show_speed(self):
        return f'Скорость автомобиля {self.name}: {self.speed} км/ч'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль {self.name} превысил скорость на {self.speed - 60} км/ч!'
        elif self.speed > 0:
            return f'Автомобиль {self.name} едет со скоростью {self.speed}'
        elif self.speed == 0:
            return self.stop()
        else:
            return 'Введены неверные данные'


class SportCar(Car):
    """Автомобиль является спортивным"""


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'Автомобиль {self.name} превысил скорость на {self.speed - 40} км/ч!'
        elif self.speed > 0:
            return f'Автомобиль {self.name} едет со скоростью {self.speed}'
        elif self.speed == 0:
            return self.stop()
        else:
            return 'Введены неверные данные'


class PoliceCar(Car):
    """Автомобиль является полицейским"""


ferrari = SportCar('Ferrari', 'Красный', 314)
dodge = PoliceCar('Dodge', 'Черно-белый', 217, True)
nissan = TownCar('Nissan', 'Белый', 75)
opel = WorkCar('Opel', 'Синий', 50)

print(ferrari.show_speed())
print(dodge.go())
print(nissan.show_speed())
print(nissan.turn('направо'))
print(dodge.stop())
