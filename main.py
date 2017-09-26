import time
import datetime
import sys

from prettytable import PrettyTable
from subprocess import call
from units.UnitFactory import UnitFactory


class Main:
    def __init__(self):
        self.timer = 0.01
        self.run = True
        self.size = 5
        self.i = 0
        self.units_list = None
        self.empty = 0
        self.start_time = ''

    def render(self):

        self.units_list = [[UnitFactory.create_unit(i, j, 1) for j in range(self.size)] for i in range(self.size)]
        self.start_time = datetime.datetime.fromtimestamp(time.time()).strftime(
            '%d.%m.%Y %H:%M:%S')
        self.i = 1
        call(["clear"])
        print("start")
        while self.run:
            self.process_iter()

    def process_iter(self):
        self.empty = 0
        self.i += 1

        current_time = datetime.datetime.fromtimestamp(time.time()).strftime(
            '%d.%m.%Y %H:%M:%S')

        table = PrettyTable(header=False, hrules=1)
        for row in self.units_list:
            table.add_row([unit.get_str() for unit in row])
            for unit in row:
                self.process_unit(unit)

        main_table = PrettyTable(header=False)
        main_table.add_row([self.timer, "Start time:\n" + self.start_time,
                            "Current time:\n" + current_time,
                            "Current iter: %d" % self.i,
                            "Empty: " + str(self.empty)])

        print(main_table)
        print(table)

        if self.empty >= self.size * self.size:
            sys.exit(0)

        print("\033[90A")
        time.sleep(self.timer)

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
