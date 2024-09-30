from sqlite3 import Connection, Cursor

from core.controll_data.cash import Cash


class Session(Cursor, Cash):
    def __init__(self, cursor: Connection) -> None:
        super().__init__(cursor)
