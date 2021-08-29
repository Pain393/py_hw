class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * 25 * 5 / 1000
        print(f'Для покрытия дорожного полотна неободимо {round(asphalt_mass)} массы асфальта')


r = Road(5000, 20)
r.asphalt_mass()