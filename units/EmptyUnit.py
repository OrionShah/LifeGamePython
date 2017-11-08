from units.Unit import *


class EmptyUnit(Unit):
    def __init__(self, x, y):
        self.size = None
        self.name = ''
        self.x = x
        self.y = y
        self.evol = None
        self.type = 0

    def get_str(self):
        return "{name:10s}\n".format(name="")

    def process_iter(self):
        return self

    def is_empty(self):
        return True

    def check_near(self, list_units):
        near = []
        xp = self.x + 1
        if xp > len(list_units)-1:
            xp = 0

        xm = self.x - 1
        if xm < 0:
            xm = len(list_units) - 1

        yp = self.y + 1
        if yp > len(list_units[self.x])-1:
            yp = 0

        ym = self.y - 1
        if ym < 0:
            ym = len(list_units[self.x]) - 1

        near.append(list_units[xm][self.y])
        near.append(list_units[xp][self.y])
        near.append(list_units[self.x][ym])
        near.append(list_units[self.x][yp])

        plus = 0
        # minus = 0
        for item in near:
            if int(item.get_type()) > 40 and item.get_size() > AGE_FROM:
                plus += 1
            # if "−" in item.get_type():
            #     minus += 1

        # print(plus)
        if plus > 2:
            return True

        return False
