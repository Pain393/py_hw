from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def tissue(self):
        pass

    def __add__(self, other):
        return self.tissue + other.tissue


class Coat(Clothes):

    @property
    def tissue(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def tissue(self):
        return 2 * self.param + 0.3


coat = Coat(650)
suit = Suit(50)
print(coat.tissue)
print(suit.tissue)
print(coat + suit)
