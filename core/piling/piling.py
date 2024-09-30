from os import environ
from typing import Any
from dotenv import load_dotenv, find_dotenv
from urllib.request import urlopen
from json import loads

from core.utilities.singleton import Singleton


class Piling(metaclass=Singleton):
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self.telegrmUrlUpdates = (
            environ.get("TELEGRAM_BOT_ROOT_URL") +
            "/getUpdates?limit=1&offset="
        )
        self.last_update_id = 0

    def start(self) -> Any:
        while True:
            update = urlopen(
                self.telegrmUrlUpdates + str(self.last_update_id)
            ).read()
            data = loads(update)["result"]
            if (not data):
                continue
            data = data[0]
            self.last_update_id = data["update_id"] + 1
            yield data
