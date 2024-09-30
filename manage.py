from core.controller.controller import Controller
import sys
from main.configuration import configurate, TABLES


def runbot():
    configurate()
    bot = Controller(TABLES)
    bot.runbot()


if (__name__ == "__main__"):
    cmd = {
        "runbot": runbot,
    }
    if (sys.argv.__len__() == 1):
        print("plug")
        exit()
    if (sys.argv[1] in cmd):
        try:
            cmd[sys.argv[1]]()
        except KeyboardInterrupt:
            print("shut down bot")
