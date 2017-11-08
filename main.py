import time
import datetime
import sys

from prettytable import PrettyTable
from subprocess import call
from units.Unit import Unit
from Table import Table


class TableRender:
    def __init__(self, table: Table):
        self.table = table
        self.run = True
        self.timer = 0.5
        self.start_time = datetime.datetime.fromtimestamp(time.time()).strftime(
            '%d.%m.%Y %H:%M:%S')
        self.i = 1

    def render(self):
        call(["clear"])
        while self.run:
            self.iteration()

    def get_header(self):
        current_time = datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y %H:%M:%S')
        main_table = PrettyTable(header=False)
        main_table.add_row([self.timer, "Start time:\n" + self.start_time,
                            "Current time:\n" + current_time,
                            "Current iter: %d" % self.i])
        return main_table

    def get_main_table(self):
        t = PrettyTable(header=False, hrules=1)
        for row in self.table.points:
            r = []
            for unit in row:
                if unit is not None:
                    r.append(unit.get_str())
                else:
                    empty_unit = '             '
                    for i in range(3):
                        empty_unit += '\n             '
                    r.append(empty_unit)
            t.add_row(r)
        return t

    def process_units(self):
        for row in self.table.points:
            for unit in row:
                if unit is not None:
                    unit.do()

    def iteration(self):
        self.process_units()
        print(self.get_header())
        print(self.get_main_table())
        print("\033[90A")
        time.sleep(self.timer)


if __name__ == "__main__":
    try:
        table = Table()
        renderer = TableRender(table)

        unit = Unit(table, 1, 1)

        renderer.render()
    except KeyboardInterrupt:
        pass
