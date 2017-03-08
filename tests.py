import time
import datetime
import sys
from random import randint

from Unit import Unit
from prettytable import PrettyTable
from subprocess import call


_old_excepthook = sys.excepthook


def myexcepthook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        run = False
    else:
        _old_excepthook(exctype, value, traceback)
sys.excepthook = myexcepthook

run = True
TIMER = 0.01

def render():
    units = [Unit(randint(0, 4), randint(0, 4)) for i in range(10)]
    # for unit in units:
    #     print(unit)

    i = 1
    call(["clear"])
    print("start")
    while run:
        print("TIMER: %fs" % TIMER)

        print(datetime.datetime.fromtimestamp(time.time()).strftime('%d.%m.%Y %H:%M:%S'))
        print("Current iter: %d" % i)
        i += 1

        table = PrettyTable(["name:", ] + [unit.get_name() for unit in units])
        table.add_row(["size: "] + [unit.get_size() for unit in units])
        for unit in units:
            unit.process_iter()

        print(table)
        print("\033[9A")
        time.sleep(TIMER)


if __name__ == "__main__":
    render()
