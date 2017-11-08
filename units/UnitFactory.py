from units.Unit import Unit
from units.EmptyUnit import EmptyUnit

from random import randint


class UnitFactory:
    @staticmethod
    def create_unit(x, y, evol):
        random = randint(0, 1000)
        if random > 500:
            unit = EmptyUnit(x, y)
        else:
            unit = Unit(x, y, evol)
        return unit
