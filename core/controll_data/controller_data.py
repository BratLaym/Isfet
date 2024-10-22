from dotenv import load_dotenv, find_dotenv
from os import environ
from sqlite3 import connect

from core.utilities.singleton import Singleton
from core.controll_data.session import Session


class ControllerData(metaclass=Singleton):
    def __init__(self, tables: dict[str, str] = dict()) -> None:
        load_dotenv(find_dotenv())
        self._connection = connect(str(environ.get("PATH_DB")))
        self._create_db(tables)

    def _create_db(self, tables: dict[str, str]):
        session = self.create_session()
        for name, table in tables.items():
            print("create:", name)
            session.execute(
                f"CREATE TABLE IF NOT EXISTS {name} ({table});"
            )
        self.commit()

    def create_session(self) -> Session:
        return Session(self._connection)

    def commit(self) -> None:
        self._connection.commit()
