from units.Unit import Unit


class EmptyUnit(Unit):
    def __init__(self, x, y):
        self.size = None
        self.name = ''
        self.x = x
        self.y = y
        self.evol = None

    def get_str(self):
        return "{name:10s}\n".format(name="")

    def process_iter(self):
        return self