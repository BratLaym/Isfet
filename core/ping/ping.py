from os import environ
from dotenv import load_dotenv, find_dotenv
from urllib.request import urlopen
from json import loads


class Ping:
    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self.telegrmUrlUpdates = (
            environ.get("TELEGRAM_BOT_ROOT_URL") +
            "/getUpdates?limit=1&offset="
        )
        self.last_update_id = 0

    def getValue(self) -> dict[str, str | dict]:
        update = urlopen(
            self.telegrmUrlUpdates + str(self.last_update_id)
        ).read()
        data = loads(update)["result"]
        if (not data):
            return -1
        data = data[0]
        self.last_update_id = data["update_id"] + 1
        return data
