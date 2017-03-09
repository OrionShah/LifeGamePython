from units.Unit import Unit
from units.EmptyUnit import EmptyUnit

from random import randint


class UnitFactory:
    @staticmethod
    def create_unit(x, y, evol):
        random = randint(0, 500)
        unit = None
        if random > 450:
            unit = EmptyUnit(x, y)
        else:
            unit = Unit(x, y, evol)
        return unit
