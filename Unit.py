import random
import uuid
from colorama import Fore, Style

class Unit:
    def __init__(self, x, y):
        self.size = 1
        self.name = str(uuid.uuid4())[2:8]
        self.x = x
        self.y = y

    def process_iter(self):
        rand = random.randint(0, 100)
        if rand > 97:
            self.size += 1

        if self.size > 10:
            self.__init__(self.x, self.y)

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

    def __str__(self):
        return "Name: {name} Coords: {x}:{y} Size: {size}".format(
            name=self.name,
            size=self.size,
            x=self.x,
            y=self.y
        )
