import time
import datetime
import sys

from prettytable import PrettyTable
from subprocess import call
from units.UnitFactory import UnitFactory

import units

_old_excepthook = sys.excepthook


def myexcepthook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        run = False
    else:
        _old_excepthook(exctype, value, traceback)
sys.excepthook = myexcepthook

run = True
TIMER = 0.01
size = 12


class Main:
    def __init__(self):
        self.i = 0
        self.units_list = None
        self.empty = 0
        self.start_time = 0

    def render(self):
        self.units_list = [[UnitFactory.create_unit(i, j, 1) for j in range(size)] for i in range(size)]
        self.start_time = datetime.datetime.fromtimestamp(time.time()).strftime(
            '%d.%m.%Y %H:%M:%S')
        self.i = 1
        call(["clear"])
        print("start")
        while run:
            self.process_iter()

    def process_iter(self):
        self.empty = 0
        self.i += 1

        current_time = datetime.datetime.fromtimestamp(time.time()).strftime(
            '%d.%m.%Y %H:%M:%S')

        table = PrettyTable(header=False, hrules=1)
        for row in self.units_list:
            table.add_row([unit.get_str() for unit in row])

        for row in self.units_list:
            for unit in row:
                self.process_unit(unit)

        main_table = PrettyTable(header=False)
        main_table.add_row([TIMER, "Start time:\n" + self.start_time,
                            "Current time:\n" + current_time,
                            "Current iter: %d" % self.i,
                            "Empty: " + str(self.empty)])

        print(main_table)
        print(table)
        if self.empty >= size * size:
            sys.exit(0)

        print("\033[90A")
        time.sleep(TIMER)

    def process_unit(self, unit):
        self.units_list[unit.x][unit.y] = unit.process_iter()
        if unit.is_empty():
            self.empty += 1
            status = unit.check_near(self.units_list)
            if status is True:
                self.units_list[unit.x][unit.y] = UnitFactory.create_unit(
                    unit.x, unit.y, 1)


if __name__ == "__main__":
    game = Main()
    game.render()
