from abc import ABC, abstractmethod

from typing import Any

class AbstractClothes(ABC):
    @property
    @abstractmethod
    def tiss_need(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def _calculate_tiss_need(self):
        pass

class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name: str, measuring: Any):
        self.name = name
        self.measuring = measuring
        self._tiss_need = None
        self._clothes.append(self)

    def _calculate_tiss_need(self):
        raise NotImplemented

    @property
    def tiss_need(self):
        if not self._tiss_need:
            self._calculate_tiss_need()

        return self._tiss_need


    @property
    def measuring(self):
        return self._measuring

    @measuring.setter
    def measuring(self, measuring):
        self._measuring = measuring
        self._tiss_need = None

    @property
    def total_tiss_need(self):

        return sum([item.tiss_need for item in self._clothes])

class Coat(Clothes):
    def _calculate_tiss_need(self):
        self._tiss_need = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self):
        return self.measuring

    @V.setter
    def V(self, size):
        self.measuring = size

    def __str__(self):
        return f'на пальто {self.measuring} размера необходимо {self.tiss_need} кв м ткани'


class Suit(Clothes):
    def _calculate_tiss_need(self):
        self._tiss_need = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self):
        return self.measuring

    @H.setter
    def H(self, height):
        self.measuring = height

    def __str__(self):
        return f'для костюма на рост {self.measuring} cm необходимо {self.tiss_need} кв м ткани'



if __name__ == '__main__':
    coat = Coat('Драповое пальто', 7)
    print(coat)
    coat.V = 12
    print(coat)

    suit = Suit('Костюм с отливом', 168)
    print(suit)
    suit.H = 175
    print(suit)

    print(coat.total_tiss_need)
    print(suit.total_tiss_need)
