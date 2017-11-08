from units import BaseUnit

class Table:
    def __init__(self, size=10):
        self.size = size
        self.points = [[None for j in range(self.size)] for i in range(self.size)]

    def add_unit(self, x, y, unit: BaseUnit):
        if self.get_point(x, y) is None:
            self.points[x][y] = unit

    def get_point(self, x, y):
        return self.points[x][y]

    def del_point(self, x, y):
        self.points[x][y] = None
