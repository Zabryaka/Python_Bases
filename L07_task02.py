from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def quant(self):
        pass


class Coat(Clothes):

    @property
    def quant(self):
        return f'{self.size / 6.5 + 0.5:.2f}'


class Suit(Clothes):

    @property
    def quant(self):
        return f'{2 * self.size + 0.3:.2f}'


co1 = Coat(48)
co2 = Coat(44)
su = Suit(1)
print(co1.quant)
print(co2.quant)
print(su.quant)
print(float(co1.quant) + float(co2.quant) + float(su.quant))
