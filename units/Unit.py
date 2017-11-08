import random
from colorama import Fore, Style

from mimesis import Personal
import units


AGE_FROM = 5
AGE_TO = 25


class BaseUnit(object):
    def __init__(self, table, x, y):
        data = Personal('en')
        self.table = table
        self.x = x
        self.y = y
        self.says = ''
        self.table.add_unit(x, y, self)
        self.name = data.name(gender='male')

    def get_str(self):
        says = '{name}({x}:{y}): {says}'.format(says=self.says, name=self.name, x=self.x, y=self.y)
        line_size = 13
        return '\n'.join([says[i:i+line_size] for i in range(0, len(says), line_size)])

    def do(self):
        pass

    def move(self):
        pass

    def check_near_point(self, x, y):
        pass

    def die(self):
        pass

    def wait(self):
        self.says = 'Thinking...'

    def eat(self):
        pass


class Unit(BaseUnit):
    def do(self):
        super().do()
        choice = random.choice(['move', 'wait', 'eat'])
        return getattr(self, choice)()

    def move(self):
        direction = random.choice(['up', 'down', 'left', 'right'])
        x = y = None
        if direction == 'up':
            x = self.x-1
            y = self.y
        elif direction == 'down':
            x = self.x + 1
            y = self.y
        elif direction == 'left':
            x = self.x
            y = self.y - 1
        elif direction == 'right':
            x = self.x
            y = self.y + 1

        if x < 0:
            x = len(self.table.points)
        if y < 0:
            y = len(self.table.points[0])
        if x+1 > len(self.table.points):
            x = 0
        if y+1 > len(self.table.points[0]):
            y = 0

        if self.table.get_point(x, y) is None:
            self.table.del_point(self.x, self.y)
            self.table.add_unit(x, y, self)
            self.says = '{dir}!'.format(dir=direction)
            self.x = x
            self.y = y
        else:
            self.says = 'I can\'t move to ({x},{y})'.format(x=x, y=y)


class OldUnit:
    def __init__(self, x, y, evol):
        person = Personal('en')
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
            return units.UnitFactory.create_unit(self.x, self.y, self.evol+1)

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
