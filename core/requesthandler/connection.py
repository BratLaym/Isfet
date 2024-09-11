from os import environ
import sqlite3
from core.patern.singleton import Singleton
from dotenv import load_dotenv, find_dotenv


class Connection(metaclass=Singleton):
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self._connection = sqlite3.connect(environ.get("PATH_DB"))

    def create_session(self) -> sqlite3.Cursor:
        return self._connection.cursor()

    def commit(self) -> None:
        self._connection.commit()
