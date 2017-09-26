import random
from colorama import Fore, Style

from elizabeth import Personal, Business
import units

# from units.UnitFactory import UnitFactory

AGE_FROM = 5
AGE_TO = 25


class Unit:
    def __init__(self, x, y, evol):
        person = Personal('ru')
        self.size = random.randint(1, 4)
        self.name = person.name(gender="female")
        self.x = x
        self.y = y
        self.evol = evol
        self.type = random.randint(30, 100)

    def process_iter(self):
        rand = random.randint(0, 100)
        max_rand = random.randint(30, 40)
        if rand > 99:
            self.size += 1

        if self.size > max_rand:
            return units.UnitFactory.UnitFactory.create_unit(self.x, self.y, self.evol+1)

        return self

    def get_base_color(self):
        color = Fore.CYAN
        if '+' in self.get_type():
            color = Fore.LIGHTCYAN_EX
        return color

    def get_name(self):
        color = self.get_base_color()
        if self.size > AGE_TO:
            color = Fore.RED

        if self.size < AGE_FROM:
            color = Fore.GREEN

        final_str = color
        final_str += self.name
        final_str += Style.RESET_ALL
        return final_str

    def get_size(self):
        return self.size

    def get_evol(self):
        return self.evol

    def get_type(self):
        return str(self.type)

    def is_empty(self):
        return False

    def check_near(self, list_units):
        return False

    def get_str(self):
        str = "{name:10s}\n{evol}:{size}T:{type}".format(
            name=self.get_name(),
            evol=self.get_evol(),
            size=self.get_size(),
            type=self.get_type()
        )
        return str

    def __str__(self):
        return "Name: {name} Coords: {x}:{y} Size: {size}".format(
            name=self.name,
            size=self.size,
            x=self.x,
            y=self.y
        )
