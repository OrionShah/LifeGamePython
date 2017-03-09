import random
from colorama import Fore, Style

from elizabeth import Personal
import units

# from units.UnitFactory import UnitFactory

class Unit:
    def __init__(self, x, y, evol):
        person = Personal('en')
        self.size = 1
        self.name = person.name(gender='female')
        self.x = x
        self.y = y
        self.evol = evol

    def process_iter(self):
        rand = random.randint(0, 1000)
        if rand > 950:
            self.size += 1

        if self.size > 9:
            return units.UnitFactory.UnitFactory.create_unit(self.x, self.y, self.evol+1)

        return self

    def get_name(self):
        final_str = ''
        if self.size > 7:
            final_str += Fore.RED

        if self.size < 3:
            final_str += Fore.GREEN

        final_str += self.name
        final_str += Style.RESET_ALL
        return final_str

    def get_size(self):
        return self.size

    def get_evol(self):
        return self.evol

    def get_str(self):
        str = "{name:10s}\n ({evol}:{size})".format(
            name=self.get_name(),
            evol=self.get_evol(),
            size=self.get_size()
        )
        return str

    def __str__(self):
        return "Name: {name} Coords: {x}:{y} Size: {size}".format(
            name=self.name,
            size=self.size,
            x=self.x,
            y=self.y
        )
