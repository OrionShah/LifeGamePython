import time
import datetime
import sys

from prettytable import PrettyTable
from subprocess import call
from units.UnitFactory import UnitFactory

_old_excepthook = sys.excepthook


def myexcepthook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        run = False
    else:
        _old_excepthook(exctype, value, traceback)
sys.excepthook = myexcepthook

run = True
TIMER = 0.01
size = 10

def render():
    units = [[UnitFactory.create_unit(i, j, 1) for j in range(size)] for i in range(size)]

    i = 1
    call(["clear"])
    print("start")
    while run:
        print("TIMER: %fs" % TIMER)

        print(datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y %H:%M:%S'))
        print("Current iter: %d" % i)
        i += 1

        table = PrettyTable(header=False, hrules=1)
        for row in units:
            table.add_row([unit.get_str() for unit in row])


        for row in units:
            for unit in row:
                units[unit.x][unit.y] = unit.process_iter()

        print(table)
        print("\033[90A")
        time.sleep(TIMER)


if __name__ == "__main__":
    render()
