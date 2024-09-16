from core.controller.controller import Controller
import sys
import sqlite3
from main.configuration import TABLES, MODULES


def runbot():
    createdb()
    bot = Controller(MODULES)
    bot.startPiling()


def dropdb():
    con: sqlite3.Connection = sqlite3.connect("data/Isfet.db")
    cur: sqlite3.Cursor = con.cursor()
    cur.execute("DROP TABLE user")
    con.commit()


def createdb():
    con: sqlite3.Connection = sqlite3.connect("data/Isfet.db")
    cur: sqlite3.Cursor = con.cursor()
    for name, table in TABLES.items():
        cur.execute(f"CREATE TABLE IF NOT EXISTS {name} ({table});")
    con.commit()


if (__name__ == "__main__"):
    cmd = {
        "runbot": runbot,
        "dropdb": dropdb,
        "createdb": createdb
    }
    if (sys.argv.__len__() == 1):
        print("plug")
        exit()
    if (sys.argv[1] in cmd):
        try:
            cmd[sys.argv[1]]()
        except KeyboardInterrupt:
            print("shut down bot")
